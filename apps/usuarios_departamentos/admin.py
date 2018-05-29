from django.contrib import admin

from .models import UsuarioDepartamento


class UsuarioDepartamentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(UsuarioDepartamento, UsuarioDepartamentoAdmin)
