from django.shortcuts import render
from django.views.generic import View
import json
from django.http import JsonResponse

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
