from django import forms
from .models import Producto, InsumosProducto
import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, Row, HTML, ButtonHolder, Submit, Button
from .custom_layout_object import Formset


class InsumosProductoForm(forms.ModelForm):

    class Meta:
        model = InsumosProducto
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Field('insumo'),
                Field('cantidad'),
                Field('DELETE'),
                css_class=f'formset_row-{formtag_prefix}'
            )
        )


InsumosProductoFormset = forms.inlineformset_factory(
    Producto, InsumosProducto, form=InsumosProductoForm,
    fields=['insumo', 'cantidad'], can_delete=True, extra=1, max_num=5)

class ProductoForm(forms.ModelForm):

    #insumo_base = forms.ModelChoiceField(queryset=Insumo.objects.filter(nombre__contains='MDF'))
    #insumo_lados = forms.ModelChoiceField(queryset=Insumo.objects.filter(nombre__contains='MDF'))

    class Meta:
        model = Producto
        exclude = ('insumos',)

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('nombre'),
                Field('descripcion'),
            ),
            Div(
                Fieldset('Medidas del producto',
                'largo', 'ancho', 'alto', 'tiempo'),
                Fieldset('Fibrofacil utilizado para el producto',
                'insumo_base', 'insumo_lados')
            ),
            Div(
                Fieldset(
                    'Agregue insumos extra',
                    Formset('insumos'),
                ),
                HTML('<br>'),
                ButtonHolder(
                    Submit('submit', 'Guardar'),
                ),
            )
        )
