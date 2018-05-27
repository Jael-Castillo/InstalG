from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Material
from .forms import MaterialForm


class MaterialCreate(CreateView):
    template_name = 'materiales/form.html'
    form_class = MaterialForm
    success_url = reverse_lazy('materiales:list')

class MaterialUpdate(UpdateView):
    model = Material
    template_name = 'materiales/form.html'
    form_class = MaterialForm
    success_url = reverse_lazy('materiales:list')
    
class MaterialList(ListView):
    model = Material
    template_name = 'materiales/list.html'

class MaterialDetail(DetailView):
    model = Material
    template_name = 'materiales/detail.html'

class MaterialDelete(DeleteView):
    model = Material
    template_name = 'materiales/delete.html'
    success_url = reverse_lazy('materiales:list')
