from django import forms

from .models import Empleado


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    def clean_codigo_postal(self):
        codigo_postal = self.cleaned_data.get("codigo_postal")

        if len(codigo_postal) != 5 or not codigo_postal.isdigit():
            raise forms.ValidationError("Escribe un código postal válido. Ej: 05032")
        return codigo_postal