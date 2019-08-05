from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .abstract_models import *

# Create your models here.
class Unidad(models.Model):
    """ Tabla de referencia para unidades de medida de insumos. """

    nombre = models.CharField(max_length=128, unique=True)
    descripcion = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Unidades"

    def __str__(self):
        return f"{self.nombre}"


class Insumo(models.Model):
    nombre = models.CharField(max_length=64, unique=True)
    descripcion = models.TextField(blank=True)
    medida = models.CharField(max_length=64)
    unidad_medida = models.ForeignKey(
        Unidad, on_delete=models.CASCADE, default=3, related_name="unidades"
    )
    precio = models.DecimalField(
        help_text="Precio en $", max_digits=6, decimal_places=2
    )
    proveedores = models.ManyToManyField("proveedores.Proveedor")

    def __str__(self):
        if self.descripcion:
            return f"{self.nombre} - {self.descripcion}"
        else:
            return self.nombre

class StockInsumo(models.Model):
    """ Contiene la cantidad de insumos """

    insumo = models.OneToOneField(Insumo, on_delete=models.CASCADE)
    cantidad = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Cantidad en Stock"
    )
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cantidad} - {self.insumo}"


class Producto(models.Model):
    """ Este modelo se refiere al Producto Genérico: Bandeja, Bastidor, Reloj """

    nombre = models.CharField(max_length=128)
    descripcion = models.TextField(blank=True)
    precio = models.PositiveIntegerField(help_text="Precio en $")
    
    # https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ManyToManyField.through_fields
    insumos = models.ManyToManyField(Insumo, 
                through="InsumosProducto", 
                through_fields=('producto', 'insumo'))

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("detailProducto", kwargs={"pk": self.pk})

    def get_image_url(self):
        img = self.productimage_set.first()
        return img.imagen.url if img else img

    @property
    def get_insumos(self):
        insumos_producto = self.insumosproducto_set.all()

        return insumos_producto


class ProductImage(models.Model):
    """Model definition for ProductImage."""

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos/", blank=True)

    class Meta:
        """Meta definition for ProductImage."""

        verbose_name = "Imagen de Producto"
        verbose_name_plural = "Imágenes de Producto"

    def __str__(self):
        """Unicode representation of ProductImage."""
        return self.producto.nombre


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
# porque ahora se crean los productos pero los insumos 
# no se guardan.
