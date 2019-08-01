from django.forms import inlineformset_factory, ModelForm, modelformset_factory
from .models import *


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        exclude = ('insumos',)

InsumosProductoFormset = inlineformset_factory(
    Producto, InsumosProducto, form=ProductoForm, can_delete=False)
