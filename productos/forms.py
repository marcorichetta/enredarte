from django.forms import inlineformset_factory, ModelForm
from .models import Producto, Insumo, InsumosProducto


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        exclude = ()

InsumosProductoFormset = inlineformset_factory(
    Producto, InsumosProducto, form=ProductoForm, extra=3)
