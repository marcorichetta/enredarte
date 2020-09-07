from django.db import models
from django.urls import reverse
from core.base_model import BaseModel
from datetime import date


# Create your models here.


class Compra(BaseModel):
    """Model definition for Compra."""

    # Un proveedor no se puede eliminar si existen compras asociadas a él
    proveedor = models.ForeignKey(
        "proveedores.Proveedor", on_delete=models.PROTECT, related_name="compras"
    )
    insumos_compra = models.ManyToManyField("productos.Insumo", through="InsumosCompra")
    detalles = models.TextField(blank=True)
    fecha_compra = models.DateField(
        default=date.today
    )  # Igual que auto_now_add pero permite cambiar la fecha

    class Meta:
        ordering = ["-fecha_compra"]

    def __str__(self) -> str:
        return f"Compra #{self.id}"

    def get_absolute_url(self) -> str:
        return reverse("compras:detail", kwargs={"pk": self.id})

    @property
    def precio_total(self):
        """ Precio de la suma de los insumos """

        return sum(insumo.precio_compra for insumo in self.insumos_comprados.all())


class InsumosCompra(BaseModel):
    """Model definition for InsumosCompra."""

    """ Si se elimina una compra
        los insumos asociados a esa compra se eliminan """
    compra = models.ForeignKey(
        Compra, on_delete=models.CASCADE, related_name="insumos_comprados"
    )
    insumo = models.ForeignKey("productos.Insumo", on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_compra = models.DecimalField(
        max_digits=6, decimal_places=2, help_text="Precio unitario"
    )

    class Meta:
        verbose_name_plural = "InsumosCompras"

    def __str__(self):
        return f"{self.cantidad} - {self.insumo.nombre}"
