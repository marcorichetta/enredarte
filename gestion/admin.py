from django.contrib import admin

from .models import (
    Proveedor,
    Insumo,
    Unidad,
    Cliente,
    Localidad,
    Provincia,
    EstadoPedido,
    Pedido,
    Producto,
    StockInsumo,
    InsumosProducto
)
# Register your models here.
# Password: enredarte


@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')

class LocalidadInline(admin.TabularInline):
    '''Tabular Inline View for Localidad'''


    model = Localidad
    min_num = 3
    max_num = 20
    extra = 1

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('provincia', 'cod_provincia')

    inlines = [
        LocalidadInline,
    ]


@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('cod_postal', 'localidad', 'provincia')
    list_filter = ('provincia',)


@admin.register(EstadoPedido)
class EstadoPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'detalles')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'email',
        'telefono',
        'calle',
        'numero',
        'localidad',
    )
    search_fields = ('nombre', 'apellido',)
    list_display_links = ('nombre',)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cuit',
        'razon_social',
        'telefono',
        'email',
        'calle',
        'numero',
        'localidad',
    )
    search_fields = ('cuit', 'razon_social',)
    list_display_links = ('cuit',)
    ordering = ('razon_social',)

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


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio')
    raw_id_fields = ('insumos',)


@admin.register(InsumosProducto)
class InsumosProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'insumo', 'cantidad')
    list_filter = ('producto', 'insumo')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha_pedido',
        'cliente',
        'estado_pedido',
        'precio_final',
    )
    list_filter = ('fecha_pedido', 'cliente', 'estado_pedido')
    raw_id_fields = ('productos_pedido',)
