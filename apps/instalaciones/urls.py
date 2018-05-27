from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', InstalacionList.as_view(), name='list'),
    url(r'^create/$', InstalacionCreate.as_view(), name='create'),
    url(r'^(?P<pk>\w+)/$', InstalacionDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', InstalacionDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', InstalacionUpdate.as_view(), name='update'),
]
