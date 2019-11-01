from django.db import models
from django.urls import reverse

# Create your models here.


class Compra(models.Model):
    """Model definition for Compra."""

    # Un proveedor no se puede eliminar si existen compras asociadas a él
    proveedor = models.ForeignKey(
        'proveedores.Proveedor', on_delete=models.PROTECT)
    insumos_compra = models.ManyToManyField(
        'productos.Insumo', through="InsumosCompra")
    detalles = models.TextField(blank=True)
    fecha_compra = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_compra']

    def __str__(self):
        return f"Compra #{self.id}"

"""     def get_absolute_url(self):
        return reverse('detailCompra', kwargs={'pk': self.id})
 """

class InsumosCompra(models.Model):
    """Model definition for InsumosCompra."""

    """ Si se elimina una compra
        los insumos asociados a esa compra se eliminan """
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    insumo = models.ForeignKey('productos.Insumo', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_compra = models.PositiveIntegerField(help_text="Precio unitario")

    class Meta:
        verbose_name_plural = 'InsumosCompras'

    def __str__(self):
        return f"{self.cantidad} - {self.insumo.nombre}"
