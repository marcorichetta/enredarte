import re
from django import forms
from productos.models import Producto, Insumo, InsumosProducto, Regular, Irregular

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    ButtonHolder,
    Div,
    Field,
    Fieldset,
    HTML,
    Hidden,
    Layout,
    Row,
    Submit,
)
from core.custom_layout_object import Formset


class ProductoIrregularForm(forms.ModelForm):
    """Form para producto irregular"""

    class Meta:
        """Meta definition for ProductoIrregularform."""

        model = Irregular
        exclude = ("insumos",)
        # fields = ('nombre', 'descripcion', 'detalles', 'tiempo', 'insumos')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 create-label"
        self.helper.field_class = "col-md-9"
        self.helper.layout = Layout(
            Div(
                Field("nombre"),
                Hidden("tipo", "irregular"),  # Campo 'tipo' oculto con valor Irregular
                Field("descripcion", style="height: 5rem"),
                Field("tiempo"),
                Field("detalles", style="height: 5rem"),
                Field("precio"),
                css_class="col-8",
            ),
            Div(Fieldset("Insumos extra", Formset("insumos")),),
            HTML("<br>"),
            ButtonHolder(Submit("submit", "Guardar Producto", css_class="btn-success")),
        )


class ProductoRegularForm(forms.ModelForm):
    """ Formulario principal del Producto. Se utiliza para la creación y update de los mismos """

    # Filtra los insumos disponibles para base y lados
    # Solo incluye los que contengan MDF
    insumo_base = forms.ModelChoiceField(
        queryset=Insumo.objects.filter(nombre__contains="MDF")
    )
    insumo_lados = forms.ModelChoiceField(
        queryset=Insumo.objects.filter(nombre__contains="MDF")
    )

    class Meta:
        model = Regular
        exclude = ("insumos",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 create-label"
        self.helper.field_class = "col-md-9"
        self.helper.layout = Layout(
            Div(
                Field("nombre"),
                Hidden("tipo", "regular"),  # Campo 'tipo' oculto con valor regular
                Field("descripcion", style="height: 5rem"),
                css_class="col-8",
            ),
            Div(
                Fieldset(
                    "Medidas",
                    Field("largo", min=0),
                    Field("ancho", min=0),
                    Field("alto", min=0),
                    "tiempo",
                    css_class="col-4",
                ),
                Fieldset(
                    "Fibrofacil utilizado",
                    "insumo_base",
                    "insumo_lados",
                    css_class="col-6",
                ),
                css_class="d-flex",
            ),
            Div(Fieldset("Insumos extra", Formset("insumos")),),
            HTML("<br>"),
            ButtonHolder(Submit("submit", "Guardar Producto", css_class="btn-success")),
        )


class CustomChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        """ Modifica las opciones que se muestran en el select generado """
        return f"{obj.descripcion} ({obj.unidad_medida})"


class InsumosProductoForm(forms.ModelForm):
    """Estructura del formulario para agregar insumos al crear un producto. """

    insumo = CustomChoiceField(queryset=Insumo.objects.all(),)

    class Meta:
        model = InsumosProducto
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
                Field("insumo"),
                Field("cantidad"),
                Field("DELETE"),
                css_class=f"formset_row-{formtag_prefix}",
            )
        )


# Formset que incluye las relaciones entre Producto e Insumo
# - Se crea 1 formset inicialmente
# - Se pueden agregar 4 más
InsumosProductoFormset = forms.inlineformset_factory(
    Producto,
    InsumosProducto,
    form=InsumosProductoForm,
    fields=["insumo", "cantidad"],
    can_delete=True,
    extra=1,
    max_num=5,
)
