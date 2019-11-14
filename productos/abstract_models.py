from django.db import models
from django.urls import reverse
import django.apps as apps

class AbstractProductClass(models.Model):
    """
    Usada para definir atributos para un tipo de producto.
    Por ejemplo, Bandejas, Bastidores, Relojes.

    Un Producto solo puede pertener a una Clase de producto.
    """

    nombre = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        abstract = True
        app_label = 'clientes'
        ordering = ['nombre']
        verbose_name = 'Clase de Producto'
        verbose_name_plural = 'Clases de Producto'
    
    def __str__(self):
        return self.nombre
    
    @property
    def has_attributes(self):
        return self.attributes.exists()


class AbstractProduct(models.Model):
    """Model definition for AbstractProduct."""

    UNICO, PADRE, HIJO = 'unico', 'padre', 'hijo'
    STRUCTURE_CHOICES = (
        (UNICO, ('Producto único')),
        (PADRE, ('Producto padre')),
        (HIJO, ('Producto hijo'))
    )

    estructura = models.CharField(max_length=10, choices=STRUCTURE_CHOICES, default=UNICO)
    cod_producto = models.CharField(max_length=64, blank=False, null=False, unique=True, 
        help_text='Código único de producto para identificación')
    
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hijos',
        verbose_name='Producto padre',
        help_text="Sólo elija un producto padre si está creando un producto hijo.\
                    Deje en blanco si este es un producto único."
        )
    
    nombre = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(blank=True)

    product_class = models.ForeignKey(
        'productos.ProductClass',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name= 'Tipo de Producto', related_name='productos',
        help_text='Elige que tipo de producto es este'
    )

    atributos = models.ManyToManyField(
        'productos.ProductAttribute',
        through='ProductAttributeValue',
        verbose_name="Atributos",
        help_text='Un atributo de producto es algo que este producto \
                    puede tener, como la altura, especificada por su clase'
    )

    class Meta:
        """Meta definition for AbstractProduct."""

        abstract = True
        app_label = 'productos'
        verbose_name = 'AbstractProduct'
        verbose_name_plural = 'AbstractProducts'

    def __str__(self):
        self.titulo

class AbstractProductAttribute(models.Model):
    """Define un atributo para una Clase de Producto
    (Lados para un reloj).
    """

    product_class = models.ForeignKey(
        'productos.ProductClass',
        blank=True,
        on_delete=models.CASCADE,
        related_name='atributos',
        null=True,
        verbose_name="Tipo de producto"
        )
    
    nombre = models.CharField(max_length=128)

     # Attribute types
    TEXT = "text"
    INTEGER = "integer"
    
    TYPE_CHOICES = (
        (TEXT, "Texto"),
        (INTEGER, "Entero"),
    )

    tipo = models.CharField(
        choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0],
        max_length=20, verbose_name="Tipo")

    class Meta:
        abstract = True
        app_label = 'clientes'
        ordering = ['nombre']
        verbose_name = 'Atributo de Producto'
        verbose_name_plural = 'Atributos de Producto'