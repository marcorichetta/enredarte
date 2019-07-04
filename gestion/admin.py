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


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cod_provincia', 'provincia')


@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'localidad', 'provincia')
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
        'detalles',
    )
    list_filter = ('localidad',)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cuit',
        'razon_social',
        'nombre_fantasia',
        'telefono',
        'email',
        'calle',
        'numero',
        'localidad',
        'detalles',
    )
    list_filter = ('localidad',)


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
        'detalles',
    )
    list_filter = ('fecha_pedido', 'cliente', 'estado_pedido')
    raw_id_fields = ('productos_pedido',)
