from django.contrib import admin
from .models import Cliente

# Register your models here.

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
        'fecha_creacion',
    )
    search_fields = ('nombre', 'apellido',)
    list_filter = ('fecha_creacion',)
    list_display_links = ('nombre',)
