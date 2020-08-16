from django.contrib import admin

from .models import Compra, InsumosCompra

# Register your models here.


class InsumoInline(admin.TabularInline):
    """Tabular Inline View for Insumo"""

    model = InsumosCompra
    min_num = 1
    max_num = 20
    extra = 1


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    """Admin View for Compra"""

    autocomplete_fields = ["proveedor"]
    list_display = ("id", "proveedor", "fecha_compra")
    list_filter = ("proveedor", "fecha_compra")
    inlines = [InsumoInline]


@admin.register(InsumosCompra)
class InsumosCompraAdmin(admin.ModelAdmin):
    """Admin View for InsumosCompra"""

    list_display = ("compra", "insumo", "cantidad", "precio_compra")
