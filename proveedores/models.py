from django.db import models
from django.urls import reverse
from .helpers import validar_cuit
from core.base_model import BaseModel
from django.core.exceptions import ValidationError

# Create your models here.


class Proveedor(BaseModel):
    razon_social = models.CharField(max_length=64)
    cuit = models.CharField(
        max_length=13,
        unique=True,
        blank=True,
        null=True,
        validators=[validar_cuit],
        help_text="Ingrese el CUIT con el siguiente formato: 20-12345678-9",
    )
    telefono = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=True)
    calle = models.CharField(max_length=64, blank=True)
    numero = models.CharField(max_length=4, blank=True)
    """ Para eliminar una localidad, primero hay que
        eliminar todos los proveedores de la misma """
    localidad = models.ForeignKey(
        "core.Localidad", on_delete=models.PROTECT, related_name="proveedores"
    )
    detalles = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self) -> str:
        return f"{self.razon_social}"

    def get_absolute_url(self) -> str:
        return reverse("proveedores:detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        """ Si el CUIT existe entre los borrados no se puede crear el proveedor."""

        if self.cuit:
            qs = Proveedor.all_objects.filter(cuit=self.cuit)

            # Si es mayor a 1 significa que existe un registro soft-deleted
            if qs.count() > 1:

                raise ValidationError(
                    "Un proveedor con el CUIT %(cuit)s ya existe",
                    code="cuit duplicado",
                    params={"cuit": self.cuit},
                )

        return super().save(*args, **kwargs)
