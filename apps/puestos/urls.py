from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', PuestoList.as_view(), name='list'),
    url(r'^create/$', PuestoCreate.as_view(), name='create'),
    url(r'^(?P<pk>\w+)/$', PuestoDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', PuestoDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', PuestoUpdate.as_view(), name='update'),
]
