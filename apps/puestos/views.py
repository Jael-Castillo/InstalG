from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Puesto
from .forms import PuestoForm


class PuestoCreate(CreateView):
    template_name = 'puestos/form.html'
    form_class = PuestoForm
    success_url = reverse_lazy('puestos:list')

class PuestoUpdate(UpdateView):
    model = Puesto
    template_name = 'puestos/form.html'
    form_class = PuestoForm
    success_url = reverse_lazy('puestos:list')
    
class PuestoList(ListView):
    model = Puesto
    template_name = 'puestos/list.html'

class PuestoDetail(DetailView):
    model = Puesto
    template_name = 'puestos/detail.html'

class PuestoDelete(DeleteView):
    model = Puesto
    template_name = 'puestos/delete.html'
    success_url = reverse_lazy('puestos:list')
