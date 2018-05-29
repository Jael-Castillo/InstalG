from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Empleado
from .forms import EmpleadoForm


class EmpleadoCreate(CreateView):
    template_name = 'empleados/form.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados:list')

class EmpleadoUpdate(UpdateView):
    model = Empleado
    template_name = 'empleados/form.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados:list')
    
class EmpleadoList(ListView):
    model = Empleado
    template_name = 'empleados/list.html'

class EmpleadoDetail(DetailView):
    model = Empleado
    template_name = 'empleados/detail.html'

class EmpleadoDelete(DeleteView):
    model = Empleado
    template_name = 'empleados/delete.html'
    success_url = reverse_lazy('empleados:list')
