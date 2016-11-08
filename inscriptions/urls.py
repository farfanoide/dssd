#
#     1. Import the include() function: from django.conf.urls import url, include
#     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# """
# from django.contrib import admin

from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^home$', TemplateView.as_view(template_name='inscriptions/home.html'), name='home'),
    url(r'^list.json$', ListInscriptionsAPI.as_view()),
    url(r'^create_paper$', PaperCreateView.as_view(), name='create_paper'),
    # url(
    #     r'^gdrive/create/(?P<file_name>.+)/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$',
    #     TemplateView.as_view(),
    #     name='gdrive_create'
    # ),
    # url(r'^presentation_date/create$', TemplateView.as_view(), name='create_date'),
]
