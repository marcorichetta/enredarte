from django.contrib import admin

from .models import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cliente',
        'precio_final',
        'detalles',
        'estado',
        'actualizado',
        'fecha_pedido',
    )
    list_filter = ('cliente', 'actualizado', 'fecha_pedido')
    raw_id_fields = ('productos_pedido',)
