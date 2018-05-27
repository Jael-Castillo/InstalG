from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^empleados/', include('apps.empleados.urls', namespace="empleados")),
    # url(r'^instalaciones/', include('apps.instalaciones.urls', namespace="instalaciones")),
    # url(r'^materiales/', include('apps.materiales.urls', namespace="materiales")),
    # url(r'^pedidos/', include('apps.pedidos.urls', namespace="pedidos")),
    url(r'^puestos/', include('apps.puestos.urls', namespace="puestos")),
    # url(r'^proveedores/', include('apps.proveedores.urls', namespace="proveedores")),
    # url(r'^usuarios/', include('apps.usuarios.urls', namespace="usuarios")),
    # url(r'^usuarios-departamentos/', include('apps.usuarios_departamentos.urls', namespace="usuarios_departamentos")),
]
