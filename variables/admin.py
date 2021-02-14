# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from .models import Variable


class VariableForm(forms.ModelForm):
    """Form definition for Variable."""

    class Meta:
        """Meta definition for Variableform."""

        model = Variable
        fields = (
            "is_removed",
            "precio_hora",
            "ganancia_fibrofacil",
            "ganancia_por_mayor",
            "ganancia_por_menor",
        )


@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):

    # https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    # Modificar el qs para que muestre los objetos que fueron eliminados
    def get_queryset(self, request):
        return Variable.all_objects.all()

    form = VariableForm

    list_display = (
        "id",
        "precio_hora",
        # "precio_pintado",
        "ganancia_por_mayor",
        "ganancia_por_menor",
        "ganancia_fibrofacil",
        # "created",
        "modified",
        # "is_removed",
    )
