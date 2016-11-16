from django.shortcuts import render
from django.views.generic import View
import json
import random
import datetime
from faker import Faker
from django.http import JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import FormView
from django.contrib import messages

from .forms import PaperForm
from .models import Paper, Author

class ListInscriptionsAPI(View):

    def get(self, request, *args, **kwargs):
        """TODO: Docstring for get.

        :request: TODO
        :*args: TODO
        :**kwargs: TODO
        :returns: TODO

        """
        return JsonResponse([
                {'author': 'Magolla', 'titulo': 'Magoola works', 'email': 'magolla@magolla.com'},
            ], safe=False)


class PaperCreateView(FormView):
    form_class = PaperForm
    success_url = reverse_lazy('inscriptions:home')
    template_name = 'inscriptions/paper_create.html'

    def form_valid(self, form):
        author = Author.objects.create(
            name=form.cleaned_data['author_name'],
            personal_email=form.cleaned_data['author_personal_email'],
            google_email=form.cleaned_data['author_google_email'],
        )

        Paper.objects.create(
            author=author,
            title=form.cleaned_data['paper_title'],
            summary=form.cleaned_data['paper_summary'],
            topic=form.cleaned_data['paper_topic'],
            presentation_type=form.cleaned_data['paper_presentation_type'],
            collaborators=form.cleaned_data['paper_collaborators']
        )
        messages.success(self.request, 'Su trabajo ha sido enviado, recibira un mail de respuesta a la brevedad')


        return super(PaperCreateView, self).form_valid(form)


class PresentationDateView(View):
    def get(self, request, *args, **kwargs):

        fake = Faker()
        presentation_date = fake.date_time_between('-1d')
        presentation_place = fake.address()

        return JsonResponse({'presentation': {
            'date': presentation_date,
            'place': presentation_place
        }})
