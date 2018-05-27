from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', EmpleadoList.as_view(), name='list'),
    url(r'^create/$', EmpleadoCreate.as_view(), name='create'),
    url(r'^(?P<pk>\w+)/$', EmpleadoDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', EmpleadoDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', EmpleadoUpdate.as_view(), name='update'),
]
