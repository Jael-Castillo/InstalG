from django.conf.urls import url

from .views import index, detail, form

urlpatterns = [
    url(r'^$', index, name="index"), #empleados/
    url(r'^(?P<pk>\d+)/$', detail, name="detail"), #empleados/1
    url(r'^form$', form, name="form"), #empleados/form
] 
