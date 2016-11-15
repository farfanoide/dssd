from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView
from django.http import HttpResponseRedirect
from oauth2client.client import OAuth2WebServerFlow, OAuth2Credentials
from django.conf.urls import url
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from .models import GdriveRepository
from .forms import GdriveShareForm, ClosePaperForm
from inscriptions.models import Paper

from apiclient.discovery import build
import httplib2


import os
host = os.environ.get('CALLBACK_HOST', 'http://localhost:8000/')

class HasGdriveRepositoryMixin(object):
    @property
    def repo(self):
        if not hasattr(self, '_repo'):
            self._repo = GdriveRepository()
        return self._repo

class HomeView(TemplateView):

    template_name = 'home.html'


class SyncGdriveView(TemplateView):

    def get(self, request, *args, **kwargs):

        auth_uri = flow.step1_get_authorize_url()

        return HttpResponseRedirect(auth_uri)


class SyncGdriveErrorView(TemplateView):
    template_name = 'error.html'


class SyncGdriveSuccessView(View):

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code', None)

        if not code:
            return HttpResponseRedirect(reverse('gsync_error'))

        credentials = flow.step2_exchange(code)
        request.session['credentials'] = credentials.to_json()

        return HttpResponseRedirect(reverse('list'))


class GdriveListView(HasGdriveRepositoryMixin, TemplateView):

    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super(GdriveListView, self).get_context_data(**kwargs)
        context['items'] = self.repo.list()
        return context


class GdriveShareView(HasGdriveRepositoryMixin, FormView):
    template_name = 'share.html'
    success_url = reverse_lazy('list')
    form_class = GdriveShareForm


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user_email = form.cleaned_data.get('user_email')
            file_id = kwargs.get('file_id')
            self.repo.share(file_id, user_email)
            messages.success(request, 'El archivo fue correctamente compartido con el usuario {0}'.format(user_email))
        else:
            return super(GdriveShareView, self).post(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('list'))


class GdriveUnshareView(HasGdriveRepositoryMixin, View):
    success_url = reverse_lazy('list')

    def get(self, request, *args, **kwargs):
        file_id = kwargs.get('file_id')
        self.repo.unshare(file_id)
        messages.success(request, 'El archivo se ha descompartido correctamente.')
        return HttpResponseRedirect(reverse('list'))


class ClosePaperView(HasGdriveRepositoryMixin, FormView):
    form_class = ClosePaperForm
    template_name = 'close_paper.html'
    success_url = reverse_lazy('gdrive:thanks')

    def get_context_data(self, **kwargs):
        context = super(ClosePaperView, self).get_context_data(**kwargs)
        context['paper'] = Paper.objects.get(gdrive_id=self.kwargs['gdrive_id'])
        return context

    def form_valid(self, form):
        self.repo.unshare(self.kwargs['gdrive_id'])
        return super(ClosePaperView, self).form_valid(form)


class GdriveCreateView(HasGdriveRepositoryMixin, View):

    def post(self, request, *args, **kwargs):
        title = self.request.POST['title']
        email = self.request.POST['email']
        gdrive_data = self.repo.create_and_share(title, email)
        gdrive_data['close_link'] = 'http://localhost:8000' + reverse('gdrive:close_paper', kwargs={'gdrive_id':gdrive_data['id']})
        return JsonResponse(gdrive_data)
