from django.contrib import admin

from .models import Puesto


class PuestoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Puesto, PuestoAdmin)
