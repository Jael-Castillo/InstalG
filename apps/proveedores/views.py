from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Proveedor
from .forms import ProveedorForm


class ProveedorCreate(CreateView):
    template_name = 'proveedores/form.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedores:list')

class ProveedorUpdate(UpdateView):
    model = Proveedor
    template_name = 'proveedores/form.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedores:list')
    
class ProveedorList(ListView):
    model = Proveedor
    template_name = 'proveedores/list.html'

class ProveedorDetail(DetailView):
    model = Proveedor
    template_name = 'proveedores/detail.html'

class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name = 'proveedores/delete.html'
    success_url = reverse_lazy('proveedores:list')
