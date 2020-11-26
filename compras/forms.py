import re

from calendario.widgets import DatePicker
from core.custom_layout_object import Formset
from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    ButtonHolder,
    Div,
    Field,
    Fieldset,
    Layout,
    Row,
    Submit,
)
from django import forms
from productos.forms import CustomChoiceField
from productos.models import Insumo

from compras.models import Compra, InsumosCompra


class CompraForm(forms.ModelForm):
    """ Formulario principal de Compras. """

    class Meta:
        model = Compra
        fields = ("proveedor", "fecha_compra", "detalles")
        widgets = {"fecha_compra": DatePicker()}

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 create-label"
        self.helper.field_class = "col-md-9"
        self.helper.layout = Layout(
            Row(
                Div(
                    Field("proveedor"),
                    Field("fecha_compra"),
                    Field("detalles", style="height: 5rem"),
                    css_class="col-6",
                ),
                Div(Fieldset("Agregar Insumos", Formset("insumos")),),
            ),
            HTML("<br>"),
            ButtonHolder(Submit("submit", "Guardar Compra", css_class="btn-success")),
        )


class InsumosCompraForm(forms.ModelForm):
    """Estructura del formulario para agregar insumos a la compra. """

    insumo = CustomChoiceField(queryset=Insumo.objects.all(),)

    class Meta:
        model = InsumosCompra
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub("-[0-9]+$", "", kwargs.get("prefix", ""))

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = "col-auto"
        self.helper.field_class = "col-auto"
        self.helper.layout = Layout(
            Row(
                Field("insumo", css_class="w-auto"),
                Field("cantidad", min=1,),
                PrependedText("precio_compra", "$", min=0,),
                Field("DELETE"),
                css_class=f"formset_row-{formtag_prefix} flex-nowrap",  # Reemplaza a formCssClass
            )
        )


# Formset que incluye las relaciones entre Compra e Insumo
# - Se crea 1 formset inicialmente
# - Se pueden agregar 4 más
InsumosCompraFormset = forms.inlineformset_factory(
    Compra,
    InsumosCompra,
    form=InsumosCompraForm,
    fields=["insumo", "cantidad", "precio_compra"],
    can_delete=True,
    extra=0,
    min_num=1,
    max_num=20,
)
