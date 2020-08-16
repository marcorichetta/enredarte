from django.db import models
from django.urls import reverse

from model_utils.models import SoftDeletableModel, TimeStampedModel

# Create your models here.


class Cliente(SoftDeletableModel, TimeStampedModel):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
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
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["nombre", "apellido"]

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def get_email(self) -> str:
        return self.email

    def get_absolute_url(self) -> str:
        return reverse("detailCliente", kwargs={"pk": self.id})
