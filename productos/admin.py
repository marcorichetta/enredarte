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

    # Autocompletion on CompraAdmin
    search_fields = ('nombre',)


@admin.register(StockInsumo)
class StockInsumoAdmin(admin.ModelAdmin):
    list_display = ('id', 'insumo', 'cantidad', 'detalles')
    list_filter = ('insumo',)


class InsumoInline(admin.TabularInline):
    '''Tabular Inline View for Insumo'''

    model = InsumosProducto
    min_num = 0
    max_num = 5
    extra = 1
    raw_id_fields = ()


class ProductImageInline(admin.TabularInline):
    '''Tabular Inline View for ProductImag'''

    model = ProductImage
    min_num = 0
    max_num = 3
    extra = 1
    raw_id_fields = ()

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'descripcion',
        'largo',
        'ancho',
        'alto',
        'tiempo',
        'insumo_base',
        'insumo_lados',
    )

    list_filter = ('insumo_base', 'insumo_lados')
    search_fields = ['id, nombre']
    inlines = [
        ProductImageInline,
        InsumoInline
    ]


@admin.register(InsumosProducto)
class InsumosProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'insumo', 'cantidad')
    list_filter = ('producto', 'insumo')
