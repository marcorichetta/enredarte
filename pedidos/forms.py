import re
from django import forms
from pedidos.models import Pedido, ProductosPedido
from calendario.widgets import DatePicker

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Fieldset,
    Div,
    Row,
    HTML,
    ButtonHolder,
    Submit,
)
from core.custom_layout_object import Formset


class PedidoForm(forms.ModelForm):
    """Form principal de Pedido."""

    class Meta:
        model = Pedido
        fields = ("cliente", "detalles", "estado", "fecha_entrega", "descuento", "pagado")
        widgets = {"fecha_entrega": DatePicker()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 create-label"
        self.helper.field_class = "col-md-8"
        self.helper.layout = Layout(
            Row(
                Div(
                    Field("cliente"),
                    Field("estado"),
                    Field("fecha_entrega"),
                    Field("detalles", style="height: 5rem"),
                    Field("descuento"),
                    Field("pagado"),
                    css_class="col-6",
                ),
                Div(
                    Fieldset(
                        "Agregar Productos",
                        Formset(
                            "productos", template="pedidos/formset_productos_pedidos.html"
                        ),
                    ),
                    css_class="col-6 flex-wrap: nowrap",
                ),
            ),
            HTML("<br>"),
            ButtonHolder(Submit("submit", "Guardar Pedido", css_class="btn-success")),
        )


class DescuentoSoloLecturaForm(PedidoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper["descuento"].update_attributes(readonly=True)


class ProductosPedidoForm(forms.ModelForm):
    """Estructura del formulario para agregar insumos a la compra. """

    class Meta:
        model = ProductosPedido
        fields = ("pedido", "producto", "cantidad")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub("-[0-9]+$", "", kwargs.get("prefix", ""))

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = "col-auto"
        self.helper.field_class = "col-auto"
        self.helper.layout = Layout(
            Row(
                Field("producto", css_class="w-auto",),
                Field("cantidad", min=1),
                Field("DELETE"),
                css_class=f"formset_row-{formtag_prefix}",  # Reemplaza a formCssClass
                style="flex-wrap: nowrap;",
            )
        )


# Formset que incluye las relaciones entre Pedido y Productos
# - Se crea 1 formset inicialmente
# - Se pueden agregar 4 más
ProductosPedidoFormset = forms.inlineformset_factory(
    Pedido,
    ProductosPedido,
    form=ProductosPedidoForm,
    fields=["producto", "cantidad"],
    can_delete=True,
    extra=0,
    min_num=1,
    max_num=20,
)
