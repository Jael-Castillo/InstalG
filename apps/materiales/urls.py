from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', MaterialList.as_view(), name='list'),
    url(r'^create/$', MaterialCreate.as_view(), name='create'),
    url(r'^(?P<pk>\w+)/$', MaterialDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', MaterialDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', MaterialUpdate.as_view(), name='update'),
]
