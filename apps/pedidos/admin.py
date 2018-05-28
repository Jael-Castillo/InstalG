from django.contrib import admin

from .models import Pedido


class PedidoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pedido, PedidoAdmin)
