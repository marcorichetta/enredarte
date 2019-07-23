from django.db import models
from django.urls import reverse

from .abstract_models import *

# Create your models here.
class Unidad(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    descripcion = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return f"{self.nombre}"

class Insumo(models.Model):
    nombre = models.CharField(max_length=64, unique=True)
    descripcion = models.TextField(blank=True)
    medida = models.CharField(max_length=64)
    unidad_medida = models.ForeignKey(
        Unidad, on_delete=models.CASCADE, default=3, related_name='unidades')
    precio = models.DecimalField(
        help_text='Precio en $', max_digits=6, decimal_places=2)
    proveedores = models.ManyToManyField('proveedores.Proveedor')

    def __str__(self):
        if self.descripcion:
            return f"{self.nombre} - {self.descripcion}"
        else:
            return self.nombre


class StockInsumo(models.Model):
    insumo = models.OneToOneField(Insumo, on_delete=models.CASCADE)
    cantidad = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='Cantidad en Stock')
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cantidad} - {self.insumo}"

class Producto(AbstractProduct):
    precio = models.DecimalField(
        help_text='Precio en $', max_digits=6, decimal_places=2)
    insumos = models.ManyToManyField(Insumo, through='InsumosProducto')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"

class InsumosProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} de {self.insumo.nombre}\
            por cada {self.producto.nombre}"

# TODO
# `forms.py` para crear productos que se relacionen
# con los inusmos mediante InsumosProducto