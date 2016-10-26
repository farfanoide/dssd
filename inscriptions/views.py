from django.shortcuts import render
from django.views.generic import View
import json
from django.http import JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import FormView

from .forms import PaperForm
from .models import Paper, Collaborator, Author

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
    success_url = reverse_lazy('home')
    template_name = 'inscriptions/paper_create.html'

    def form_valid(self, form):
        import pdb; pdb.set_trace()  # XXX BREAKPOINT

        Paper.objects.create()
        Author.objects.create()

        return super(PaperCreateView, self).form_valid(form)
