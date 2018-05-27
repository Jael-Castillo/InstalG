from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Instalacion
from .forms import InstalacionForm


class InstalacionCreate(CreateView):
    template_name = 'instalaciones/form.html'
    form_class = InstalacionForm
    success_url = reverse_lazy('instalaciones:list')

class InstalacionUpdate(UpdateView):
    model = Instalacion
    template_name = 'instalaciones/form.html'
    form_class = InstalacionForm
    success_url = reverse_lazy('instalaciones:list')
    
class InstalacionList(ListView):
    model = Instalacion
    template_name = 'instalaciones/list.html'

class InstalacionDetail(DetailView):
    model = Instalacion
    template_name = 'instalaciones/detail.html'

class InstalacionDelete(DeleteView):
    model = Instalacion
    template_name = 'instalaciones/delete.html'
    success_url = reverse_lazy('instalaciones:list')
