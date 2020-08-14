from django.contrib import admin

from .models import Pedido, ProductosPedido


class ProductoInline(admin.TabularInline):
    """Tabular Inline View for Producto"""

    model = ProductosPedido
    min_num = 1
    max_num = 20
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cliente",
        "precio_final",
        "detalles",
        "estado",
        "actualizado",
        "fecha_pedido",
    )
    list_filter = ("cliente", "actualizado", "fecha_pedido")
    autocomplete_fields = ["productos_pedido"]

    inlines = [ProductoInline]
