from django import forms

from .models import UsuarioDepartamento


class UsuarioDepartamentoForm(forms.ModelForm):
    class Meta:
        model = UsuarioDepartamento
        fields = '__all__'
