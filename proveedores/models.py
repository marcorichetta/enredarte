from django.db import models
from django.urls import reverse
from .helpers import validar_cuit
from core.base_model import BaseModel

# Create your models here.


class Proveedor(BaseModel):
    razon_social = models.CharField(max_length=64)
    cuit = models.CharField(
        max_length=13,
        unique=True,
        validators=[validar_cuit],
        help_text="Ingrese el CUIT con el siguiente formato: 20-12345678-9",
        blank=True,
    )
    telefono = models.CharField(max_length=64)
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
