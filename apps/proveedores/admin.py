from django.contrib import admin

from .models import Proveedor


class ProveedorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Proveedor, ProveedorAdmin)
