from django.db import models
from django.urls import reverse
from decimal import Decimal
from django.core.validators import MinValueValidator
from model_utils import Choices
from core.base_model import BaseModel

from variables.models import Variable

# Modelos


class Unidad(BaseModel):
    """ Tabla de referencia para unidades de medida de insumos. """

    nombre = models.CharField(max_length=128, unique=True)
    descripcion = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Unidades"

    def __str__(self):
        return f"{self.nombre}"


class Insumo(BaseModel):
    nombre = models.CharField(max_length=64, unique=True)
    descripcion = models.TextField(blank=True)
    medida = models.DecimalField(
        help_text="Medida del insumo",
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.0"))],
    )
    # Si se elimina una Unidad de medida asociada
    # a un Insumo se pone el Id de la medida por defecto
    unidad_medida = models.ForeignKey(
        Unidad, on_delete=models.SET_DEFAULT, default=3, related_name="unidades"
    )
    precio = models.DecimalField(
        help_text="Precio de compra al proveedor en $",
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.0"))],
    )
    proveedores = models.ManyToManyField(
        "proveedores.Proveedor",
        related_name="insumos",
        help_text="Proveedores que venden este insumo",
    )

    def __str__(self):
        return self.nombre

    @property
    def precio_m2(self) -> float:
        """
            Precio Insumo x Ganancia FF / m2 de una plancha de 380x280cm == (10.64 m2)

            Devuelve el precio redondeado de m2 del insumo
        """
        return (
            self.precio * Variable.objects.get(pk=1).ganancia_fibrofacil / Decimal(10.64)
        )

    @property
    def precio_recorte(self) -> float:
        """ Precio del m2 * 2

            Utilizado para la venta de recortes de Fibrofacil """
        return self.precio_m2 * 2


class StockInsumo(models.Model):
    """ Contiene la cantidad de insumos """

    # Si se elimina un insumo su stock también es borrado
    insumo = models.OneToOneField(Insumo, on_delete=models.CASCADE)
    cantidad = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Cantidad en Stock",
        validators=[MinValueValidator(Decimal("0.0"))],
    )
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cantidad} - {self.insumo}"

    def get_absolute_url(self):
        return reverse("productos:detail", kwargs={"pk": self.pk})


class Producto(BaseModel):
    """ Este modelo se refiere al Producto Genérico: Bandeja, Bastidor, Reloj """

    TIPOS = Choices(("regular", "Regular"), ("irregular", "Irregular"))

    ### Campos comunes

    tipo = models.CharField(max_length=20, choices=TIPOS, default=TIPOS.regular)
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField(blank=True)
    tiempo = models.PositiveIntegerField(
        default=30, help_text="Minutos para realizar el producto"
    )

    # https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ManyToManyField.through_fields
    insumos = models.ManyToManyField(
        Insumo, through="InsumosProducto", through_fields=("producto", "insumo")
    )

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("productos:detail", kwargs={"pk": self.pk})

    def image_url(self):
        """ Devuelve la url de la 1ra imagen si es que existe """
        img = self.images.first()
        return img.imagen.url if img else img

    def get_precio(self) -> float:
        """
        Devuelve el precio total de un producto independientemente de su tipo
        """

        if self.tipo == self.TIPOS.irregular:
            # Accede a la instancia del modelo Irregular y devuelve el campo 'precio'
            return self.irregular.precio

        return self.regular.precio_venta_terminado()

    @property
    def get_insumos(self):
        return self.insumos_por_producto.all()


class Regular(Producto):
    """Producto Regular."""

    largo = models.DecimalField(
        default=0,
        help_text="Largo en cm",
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(Decimal("0.0"))],
    )
    ancho = models.DecimalField(
        default=0,
        help_text="Ancho en cm",
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(Decimal("0.0"))],
    )
    alto = models.DecimalField(
        default=0,
        help_text="Alto en cm",
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(Decimal("0.0"))],
    )

    # Default - MDF-3mm
    insumo_base = models.ForeignKey(
        Insumo,
        on_delete=models.PROTECT,
        related_name="BaseInsumo",
        default=1,
        help_text="Insumo utilizado para la base",
    )

    # Default - MDF-5mm
    insumo_lados = models.ForeignKey(
        Insumo,
        on_delete=models.PROTECT,
        related_name="LadoInsumo",
        default=2,
        help_text="Insumo utilizado para los lados",
    )

    class Meta:
        """Meta definition for Regular."""

        verbose_name = "Producto Regular"
        verbose_name_plural = "Productos Regulares"

    def __str__(self):
        return f"{self.nombre} ({self.tipo.capitalize()})"

    # TODO
    # Función que calcule todos los precios y los devuelva en un array
    # def super_precio(self):
    #     variables: Variable = Variable.objects.first()
    #     return [precio_costo, precio_venta_crudo, precio_venta_terminado]

    def precio_costo(self, variables) -> float:
        """ Calcula el precio de costo de un producto en base a las
            medidas del mismo, a los insumos utilizados y al tiempo que lleva
            producirlo. """
        precioBase = (self.largo / 100) * (self.ancho / 100) * self.insumo_base.precio_m2

        precioLatCorto = (
            (self.ancho / 100) * (self.alto / 100) * self.insumo_lados.precio_m2
        )

        precioLatLargo = (
            (self.largo / 100) * (self.alto / 100) * self.insumo_lados.precio_m2
        )

        horas: float = self.tiempo / 60

        # Castear a decimal para poder multiplicar con otro decimal
        precio_tiempo = Decimal(horas) * variables.precio_hora

        # Precio de los insumos extra que usa el producto
        precio_insumos = sum(
            insumo.precio_insumos for insumo in self.insumos_por_producto.all()
        )

        return (
            precioBase + precioLatCorto + precioLatLargo + precio_tiempo + precio_insumos
        )

    def precio_venta_crudo(self) -> float:
        """ Calcula el precio de venta al público del producto crudo """
        variables: Variable = Variable.objects.get(pk=1)

        # Precio costo * % de ganancia
        return self.precio_costo(variables) * ((variables.ganancia_por_menor / 100) + 1)

    def precio_terminado(self, variables: Variable) -> float:
        """ Calcula el precio del producto terminado, sin la ganancia """

        tiempo_terminado = (self.tiempo * 2) / 60

        precio_tiempo_terminado = Decimal(tiempo_terminado) * variables.precio_hora

        return (
            self.precio_costo(variables)
            + variables.precio_pintado
            + precio_tiempo_terminado
        )

    def precio_venta_terminado(self) -> float:
        """ Calcula el precio de venta al público del producto terminado """
        variables: Variable = Variable.objects.get(pk=1)

        # Precio terminado * % de ganancia
        return self.precio_terminado(variables) * (
            (variables.ganancia_por_menor / 100) + 1
        )


class Irregular(Producto):
    """Producto Irregular."""

    detalles = models.TextField(help_text="Detalles de armado del producto", blank=True)
    precio = models.DecimalField(
        help_text="Precio de venta del producto en $",
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.0"))],
    )

    class Meta:
        """Meta definition for Irregular."""

        permissions = [
            ("change_product_price", "Can modify an Irregular product price"),
        ]

        verbose_name = "Producto Irregular"
        verbose_name_plural = "Productos Irregulares"

    def __str__(self):
        return f"{self.nombre} ({self.tipo.capitalize()})"


class ProductImage(BaseModel):
    """ Este modelo existe para cargar 1 o más imágenes de un solo producto """

    # Si se elimina un Producto su imagen también se borra
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name="images"
    )
    imagen = models.ImageField(upload_to="productos/", blank=True)

    class Meta:
        verbose_name = "Imagen de Producto"
        verbose_name_plural = "Imágenes del Producto"

    def __str__(self):
        """Unicode representation of ProductImage."""
        return self.producto.nombre


class InsumosProducto(BaseModel):
    """ Modelo intermedio que guarda la cantidad de insumos necesarios para un producto """

    # Misma lógica que ProductosPedido
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name="insumos_por_producto"
    )
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.DecimalField(
        default=0,
        max_digits=4,
        decimal_places=1,
        validators=[MinValueValidator(Decimal("0.0"))],
    )

    class Meta:
        verbose_name = "Insumo del Producto"
        verbose_name_plural = "Insumos del Producto"

    def __str__(self):
        return f"{self.cantidad} {self.insumo.unidad_medida} de {self.insumo.nombre}"

    @property
    def precio_insumos(self) -> float:
        """ Calcula el precio total de cada insumo del producto """
        return self.cantidad * self.insumo.precio
