from django import forms

from .models import Puesto


class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = '__all__'
