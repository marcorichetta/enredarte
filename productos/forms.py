from django import forms
from .models import *


class ProductoForm(forms.ModelForm):

    insumo_base = forms.ModelChoiceField(queryset=Insumo.objects.filter(nombre__contains='MDF'))
    insumo_lados = forms.ModelChoiceField(queryset=Insumo.objects.filter(nombre__contains='MDF'))

    class Meta:
        model = Producto
        exclude = ('insumos',)


InsumosProductoFormset = forms.inlineformset_factory(
    Producto, InsumosProducto, form=ProductoForm, can_delete=False)
