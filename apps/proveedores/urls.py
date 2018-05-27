from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', ProveedorList.as_view(), name='list'),
    url(r'^create/$', ProveedorCreate.as_view(), name='create'),
    url(r'^(?P<pk>\w+)/$', ProveedorDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', ProveedorDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', ProveedorUpdate.as_view(), name='update'),
]
