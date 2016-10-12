#
#     1. Import the include() function: from django.conf.urls import url, include
#     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# """
# from django.contrib import admin

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^list.json$', ListInscriptionsAPI.as_view()),
]
