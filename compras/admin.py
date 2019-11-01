from django.contrib import admin

from .models import Compra, InsumosCompra

# Register your models here.

class InsumoInline(admin.TabularInline):
    '''Tabular Inline View for Insumo'''

    model = InsumosCompra
    min_num = 3
    max_num = 20
    extra = 1

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    '''Admin View for Compra'''

    list_display = (
        'id',
        'proveedor',
        'detalles',
        'fecha_compra',
    )
    list_filter = ('proveedor', 'fecha_compra')
    inlines = [
        InsumoInline,
    ]

    autocomplete_fields = ['insumos_compra']

@admin.register(InsumosCompra)
class InsumosCompraAdmin(admin.ModelAdmin):
    '''Admin View for InsumosCompra'''

    list_display = (
        'compra',
        'insumo',
        'cantidad',
        'precio_compra'
    )