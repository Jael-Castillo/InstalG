from django.contrib import admin

from .models import Instalacion


class InstalacionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Instalacion, InstalacionAdmin)
