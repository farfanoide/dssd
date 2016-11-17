from django.conf.urls import url
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    # url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^sync_gdrive/$', SyncGdriveView.as_view(), name='sync'),
    # url(r'^sync_gdrive_success/$', SyncGdriveSuccessView.as_view()),
    # url(r'^sync_gdrive_error/$', SyncGdriveErrorView.as_view(), name='gsync_error'),
    # url(r'^list/$', GdriveListView.as_view(), name='list'),
    # url(r'^(?P<file_id>.+)/share/$', GdriveShareView.as_view(), name='share'),
    # url(r'^(?P<file_id>.+)/unshare/$', GdriveUnshareView.as_view(), name='unshare'),

    url(r'^close_paper/(?P<gdrive_id>.+)$', ClosePaperView.as_view(), name='close_paper'),

    url(r'^create$',
        GdriveCreateView.as_view(),
        name='create',
        ),
    url(r'^thanks$', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    url(r'^create_book$', GdriveCreateBook.as_view(), name='create_book'),

]

