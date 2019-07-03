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

admin.site.register(Proveedor)
admin.site.register(Insumo)
admin.site.register(Unidad)
admin.site.register(Cliente)
admin.site.register(Localidad)
admin.site.register(Provincia)
admin.site.register(EstadoPedido)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(StockInsumo)
admin.site.register(InsumosProducto)