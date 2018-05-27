from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import UsuarioDepartamento
from .forms import UsuarioDepartamentoForm


class UsuarioDepartamentoCreate(CreateView):
    template_name = 'usuarios_departamentos/form.html'
    form_class = UsuarioDepartamentoForm
    success_url = reverse_lazy('usuarios_departamentos:list')

class UsuarioDepartamentoUpdate(UpdateView):
    model = UsuarioDepartamento
    template_name = 'usuarios_departamentos/form.html'
    form_class = UsuarioDepartamentoForm
    success_url = reverse_lazy('usuarios_departamentos:list')
    
class UsuarioDepartamentoList(ListView):
    model = UsuarioDepartamento
    template_name = 'usuarios_departamentos/list.html'
    context_object_name = 'usuario_departamento_list'

class UsuarioDepartamentoDetail(DetailView):
    model = UsuarioDepartamento
    template_name = 'usuarios_departamentos/detail.html'
    context_object_name = 'usuario_departamento'

class UsuarioDepartamentoDelete(DeleteView):
    model = UsuarioDepartamento
    template_name = 'usuarios_departamentos/delete.html'
    success_url = reverse_lazy('usuarios_departamentos:list')
    context_object_name = 'usuario_departamento'
