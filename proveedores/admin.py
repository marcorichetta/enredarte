from django.contrib import admin

from .models import Proveedor
# Register your models here.

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
