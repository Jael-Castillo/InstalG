from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', PedidoList.as_view(), name='list'),
    url(r'^create/$', PedidoCreate.as_view(), name='create'),
    url(r'^(?P<pk>\w+)/$', PedidoDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', PedidoDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', PedidoUpdate.as_view(), name='update'),
]
