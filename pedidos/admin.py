# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Pedido, ProductosPedido, OrdenTrabajo


class ProductoInline(admin.TabularInline):
    """Tabular Inline View for Producto"""

    model = ProductosPedido
    min_num = 1
    max_num = 20
    extra = 1
    exclude = ("is_removed",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Pedido.all_objects.all()

    list_display = (
        "id",
        "usuario",
        "cliente",
        "precio_total",
        "detalles",
        "estado",
        "fecha_entrega",
        "created",
        "modified",
        "is_removed",
    )
    list_filter = ("cliente", "fecha_entrega")
    autocomplete_fields = ["productos_pedido"]

    inlines = [ProductoInline]


@admin.register(ProductosPedido)
class ProductosPedidoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return ProductosPedido.all_objects.all()

    list_display = (
        "id",
        "created",
        "modified",
        "is_removed",
        "pedido",
        "producto",
        "cantidad",
    )
    list_filter = ("created", "modified", "is_removed", "pedido", "producto")


@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return OrdenTrabajo.all_objects.all()

    list_display = (
        "id",
        "pedido",
        "estado",
        "detalles",
        "created",
        "modified",
        "is_removed",
    )
    list_filter = (
        "created",
        "modified",
        "is_removed",
        "pedido",
    )
