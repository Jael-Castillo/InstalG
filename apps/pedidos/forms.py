from django import forms

from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['empleado', 'instalacion', 'fecha', 'hora']

        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'},  format='%Y-%m-%d'),
            'hora': forms.TimeInput(attrs={'type': 'time'},  format='%H:%M'),
        }
