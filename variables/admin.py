# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Variable


@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'precio_hora',
        'precio_pintado',
        'ganancia_por_mayor',
        'ganancia_por_menor',
        'ganancia_fibrofacil',
    )
