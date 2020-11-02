from django.db import models
from django.urls import reverse
from core.base_model import BaseModel
from proveedores.helpers import validar_cuit
from django.core.exceptions import ValidationError


class Cliente(BaseModel):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    cuit = models.CharField(
        max_length=13,
        unique=True,
        blank=True,
        null=True,  # Es necesario ya que el cuit es unique
        validators=[validar_cuit],
        help_text="Ingrese el CUIT con el siguiente formato: 20-12345678-9",
    )
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=64, blank=True)
    calle = models.CharField(max_length=64, blank=True)
    numero = models.CharField(max_length=6, blank=True)
    """ Para eliminar una localidad, primero hay que
        eliminar todos los clientes de la misma """
    localidad = models.ForeignKey(
        "core.Localidad", on_delete=models.PROTECT, related_name="clientes"
    )

    detalles = models.TextField(blank=True)

    class Meta:
        ordering = ["nombre", "apellido"]

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def save(self, *args, **kwargs):
        """ Si el CUIT existe entre los borrados no se puede crear el cliente."""

        if self.cuit:
            qs = Cliente.all_objects.filter(cuit=self.cuit)

            # Si es mayor a 1 significa que existe un registro soft-deleted
            if qs.count() > 1:

                raise ValidationError(
                    "Un cliente con el CUIT %(cuit)s ya existe",
                    code="cuit duplicado",
                    params={"cuit": self.cuit},
                )

        return super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("clientes:detail", kwargs={"pk": self.id})

    def get_email(self) -> str:
        return self.email
