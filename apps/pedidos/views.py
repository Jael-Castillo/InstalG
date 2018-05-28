from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core import serializers

from apps.materiales.models import Material
from .models import Pedido, DetallePedido
from .forms import PedidoForm


class PedidoCreate(CreateView):
    template_name = 'pedidos/form.html'
    form_class = PedidoForm
    success_url = reverse_lazy('pedidos:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        materiales = Material.objects.all()
        context['materiales'] = materiales
        context['materiales_json'] = serializers.serialize('json', list(materiales), fields=('nombre',))
        return context

    # def form_valid(self, form):
    #     pedido = form.save()

    #     for material in form.cleaned_data['materiales']:
    #         DetallePedido.objects.create(pedido=pedido.pk, material=material)

    #     return reverse_lazy('pedidos:detail', (pedido.pk,))

class PedidoUpdate(UpdateView):
    model = Pedido
    template_name = 'pedidos/form.html'
    form_class = PedidoForm
    success_url = reverse_lazy('pedidos:list')
    
class PedidoList(ListView):
    model = Pedido
    template_name = 'pedidos/list.html'

class PedidoDetail(DetailView):
    model = Pedido
    template_name = 'pedidos/detail.html'

class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'pedidos/delete.html'
    success_url = reverse_lazy('pedidos:list')
