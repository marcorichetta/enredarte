from django.db import models
from django.urls import reverse
from decimal import Decimal

from variables.models import Variable

from .abstract_models import *

### Variables

v = Variable.objects.first() # Sólo un registro con todas las variables

precio_hora = v.precio_hora
precio_pintado = v.precio_pintado
ganancia_por_mayor = v.ganancia_por_mayor
ganancia_por_menor = v.ganancia_por_menor
ganancia_fibrofacil = v.ganancia_fibrofacil

### Modelos

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
    # Si se elimina una Unidad de medida asociada
    # a un Insumo se pone el Id de la medida por defecto
    unidad_medida = models.ForeignKey(
        Unidad, on_delete=models.SET_DEFAULT, default=3, related_name="unidades"
    )
    precio = models.DecimalField(
        help_text="Precio de compra al proveedor en $", max_digits=6, decimal_places=2
    )
    proveedores = models.ManyToManyField("proveedores.Proveedor")

    def __str__(self):
        if self.descripcion:
            return f"{self.nombre} - {self.descripcion}"
        else:
            return self.nombre

    @property
    def get_precio_m2(self):
        """ Precio Insumo x Ganancia FF / m2 de una plancha (380x280cm)

            Devuelve el precio redondeado de m2 del insumo"""
        return round(self.precio * ganancia_fibrofacil / Decimal(10.64))

    @property
    def get_precio_recorte(self):
        """ Precio del m2 * 2

            Utilizado para la venta de recortes de Fibrofacil """
        return self.get_precio_m2 * 2


class StockInsumo(models.Model):
    """ Contiene la cantidad de insumos """

    # Si se elimina un insumo su stock también es borrado
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
    largo = models.DecimalField(default=0,
                                help_text='Largo en cm', max_digits=3, decimal_places=1)
    ancho = models.DecimalField(default=0,
                                help_text='Ancho en cm', max_digits=3, decimal_places=1)
    alto = models.DecimalField(default=0,
                               help_text='Alto en cm', max_digits=3, decimal_places=1)
    tiempo = models.PositiveIntegerField(default=30,
                                         help_text="Minutos para realizar el producto")

    # Default - MDF-3mm
    insumo_base = models.ForeignKey(
        Insumo, on_delete=models.PROTECT, related_name="BaseInsumo", default=1,
        help_text="Insumo utilizado para la base")

    # Default - MDF-5mm
    insumo_lados = models.ForeignKey(
        Insumo, on_delete=models.PROTECT, related_name="LadoInsumo", default=2,
        help_text="Insumo utilizado para los lados")

    # https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ManyToManyField.through_fields
    insumos = models.ManyToManyField(Insumo,
                                     through="InsumosProducto",
                                     through_fields=('producto', 'insumo'))

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"

    def get_absolute_url(self):
        return reverse("detailProducto", kwargs={"pk": self.pk})

    def get_image_url(self):
        """ Devuelve la url de la 1ra imagen si es que existe """
        img = self.images.first()
        return img.imagen.url if img else img

    @property
    def get_precio_costo(self):
        """ Calcula el precio de costo de un producto en base a las
            medidas del mismo, a los insumos utilizados y al tiempo que lleva
            producirlo. """
        precioBase = (self.largo / 100) * (self.ancho / 100) * self.insumo_base.get_precio_m2

        precioLatCorto = (self.ancho / 100) * (self.alto / 100) * self.insumo_lados.get_precio_m2

        precioLatLargo = (self.largo / 100) * (self.alto / 100) * self.insumo_lados.get_precio_m2

        precio_tiempo = (self.tiempo / 60) * precio_hora

        costo = int(precioBase) + int(precioLatCorto) + \
            int(precioLatLargo) + int(precio_tiempo)

        return costo

    @property
    def get_precio_venta_crudo(self):
        """ Calcula el precio de venta al público del producto crudo """

        # Precio costo * % de ganancia
        return round(self.get_precio_costo * ((ganancia_por_menor / 100) + 1))

    @property
    def get_precio_terminado(self):
        """ Calcula el precio del producto terminado, sin la ganancia """

        precio_apliques = 20
        precio_tiempo_terminado = int((self.tiempo * 2) / 60 * precio_hora)

        return self.get_precio_costo + precio_pintado + precio_apliques + precio_tiempo_terminado

    @property
    def get_precio_venta_terminado(self):
        """ Calcula el precio de venta al público del producto terminado """

        # Precio terminado * % de ganancia
        return round(self.get_precio_terminado * ((ganancia_por_menor / 100) + 1))

    @property
    def get_insumos(self):
        insumos_producto = self.insumosproducto_set.all()

        return insumos_producto


class ProductImage(models.Model):
    """ Este modelo existe para cargar 1 o más imágenes de un solo producto """

    # Si se elimina un Producto su imagen también se borra
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='images')
    imagen = models.ImageField(upload_to="productos/", blank=True)

    class Meta:
        verbose_name = "Imagen de Producto"
        verbose_name_plural = "Imágenes de Producto"

    def __str__(self):
        """Unicode representation of ProductImage."""
        return self.producto.nombre


class InsumosProducto(models.Model):

    # Misma lógica que ProductosPedido
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} de {self.insumo.nombre}\
            por cada {self.producto.nombre}"
