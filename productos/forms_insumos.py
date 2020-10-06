from productos.models import Insumo
from django import forms
from dal import autocomplete
from proveedores.models import Proveedor


class InsumoForm(forms.ModelForm):
    proveedores = forms.ModelMultipleChoiceField(
        label="Proveedores",
        required=False,
        queryset=Proveedor.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url="proveedores:autocomplete",
            attrs={
                "data-placeholder": "Seleccione uno o más proveedores",
                "data-width": "30em",
            },
        ),
    )

    descripcion = forms.CharField(
        required=False, widget=forms.Textarea(attrs={"rows": 5, "cols": 40})
    )

    class Meta:
        model = Insumo
        fields = (
            "nombre",
            "descripcion",
            "medida",
            "unidad_medida",
            "precio",
            "proveedores",
        )
