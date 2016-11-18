from django.conf.urls import url
from django.views.generic import TemplateView

from .views import *

urlpatterns = [

    url(r'^close_paper/(?P<gdrive_id>.+)$', ClosePaperView.as_view(), name='close_paper'),

    url(r'^create$',
        GdriveCreateView.as_view(),
        name='create',
        ),
    url(r'^thanks$', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    url(r'^create_book$', GdriveCreateBook.as_view(), name='create_book'),
    url(r'^show_book/(?P<gdrive_id>.+)$', ShowPdfView.as_view(), name='show_book'),
]

