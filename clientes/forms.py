from clientes.models import Cliente
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class ClienteForm(ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Cliente
        fields = (
            "nombre",
            "apellido",
            "cuit",
            "telefono",
            "email",
            "calle",
            "numero",
            "localidad",
        )

    def clean_cuit(self):
        """ Validar no existe un cliente soft-deleted con el mismo CUIT"""

        cuit = self.cleaned_data.get("cuit")

        modelo = self.Meta.model

        # Validación sólo para casos de soft-delete
        # Si existe y no fue borrado se muestra la validación por defecto de Django
        qs = modelo.all_objects.filter(is_removed=True).filter(cuit=cuit)

        if qs.exists():
            error = ValidationError(
                "Un cliente con el CUIT %(cuit)s ya existe. Por favor avise al administrador.",
                code="cuit duplicado",
                params={"cuit": cuit},
            )

            self.add_error("cuit", error)

        return cuit
