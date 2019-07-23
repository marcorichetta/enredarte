from django.contrib import admin

from .models import (
    Localidad,
    Provincia,
)
# Register your models here.
# Password: enredarte

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

""" @admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha_pedido',
        'cliente',
        'estado_pedido',
        'precio_final',
    )
    list_filter = ('fecha_pedido', 'cliente', 'estado_pedido')
    raw_id_fields = ('productos_pedido',) """
