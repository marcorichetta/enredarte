from django.contrib import admin

from .models import (
    Insumo,
    Unidad,
    Producto,
    StockInsumo,
    InsumosProducto,
    ProductImage,
)
# Register your models here.

@admin.register(ProductImage)
class ProductImage(admin.ModelAdmin):
    list_display = ('producto', 'imagen')
@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'descripcion',
        'medida',
        'unidad_medida',
        'precio',
    )
    list_filter = ('unidad_medida',)
    raw_id_fields = ('proveedores',)


@admin.register(StockInsumo)
class StockInsumoAdmin(admin.ModelAdmin):
    list_display = ('id', 'insumo', 'cantidad', 'detalles')
    list_filter = ('insumo',)

class InsumoInline(admin.TabularInline):
    '''Tabular Inline View for Insumo'''

    model = InsumosProducto
    min_num = 3
    max_num = 20
    extra = 1
    raw_id_fields = ()

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio')
    raw_id_fields = ('insumos',)
    inlines = [
        InsumoInline
    ]


@admin.register(InsumosProducto)
class InsumosProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'insumo', 'cantidad')
    list_filter = ('producto', 'insumo')
