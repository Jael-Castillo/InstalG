from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', UsuarioDepartamentoList.as_view(), name='list'),
    url(r'^create/$', UsuarioDepartamentoCreate.as_view(), name='create'),
    url(r'^(?P<pk>\w+)/$', UsuarioDepartamentoDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', UsuarioDepartamentoDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', UsuarioDepartamentoUpdate.as_view(), name='update'),
]
