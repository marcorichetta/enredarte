from django.forms import inlineformset_factory, ModelForm, modelformset_factory
from .models import *


class VarianteForm(ModelForm):
    class Meta:
        model = Variante
        fields = ('producto', 'nombre', 'precio', 'precio_venta', 'stock')

VarianteFormSet = modelformset_factory(Variante, form=VarianteForm, extra=1)

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        exclude = ('insumos',)

InsumosProductoFormset = inlineformset_factory(
    Producto, InsumosProducto, form=ProductoForm, can_delete=False)
