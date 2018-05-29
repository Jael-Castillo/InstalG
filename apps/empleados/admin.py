from django.contrib import admin

from .models import Empleado


class EmpleadoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Empleado, EmpleadoAdmin)
