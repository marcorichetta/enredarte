from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MinValueValidator
from decimal import Decimal
from datetime import date

from core.base_model import BaseModel


class Pedido(BaseModel):

    CREADO = 0
    EN_PROCESO = 1
    LISTO = 2
    ENTREGADO = 3
    CANCELADO = 4

    ESTADO_PEDIDO_CHOICES = (
        (CREADO, "Creado"),
        (EN_PROCESO, "En proceso"),
        (LISTO, "Listo para entrega"),
        (ENTREGADO, "Entregado"),
        (CANCELADO, "Cancelado"),
    )

    usuario = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
        help_text="Usuario que registra el pedido",
    )
    # Un cliente no se puede eliminar si tiene pedidos asociados
    cliente = models.ForeignKey(
        "clientes.Cliente", on_delete=models.PROTECT, related_name="clientes"
    )
    productos_pedido = models.ManyToManyField(
        "productos.Producto", through="ProductosPedido"
    )
    precio_total = models.DecimalField(
        help_text="Precio en $",
        max_digits=6,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal("0.0"))],
    )
    descuento = models.DecimalField(
        help_text="% de descuento.",
        max_digits=2,
        decimal_places=0,
        default=0,
        validators=[MinValueValidator(Decimal("0.0"))],
    )
    detalles = models.TextField(blank=True)
    estado = models.IntegerField(default=CREADO, choices=ESTADO_PEDIDO_CHOICES)
    pagado = models.BooleanField(default=False, verbose_name="Pagado")
    fecha_pedido = models.DateField(default=date.today, verbose_name="Fecha de pedido")
    fecha_entrega = models.DateField(verbose_name="Fecha de entrega estimada", blank=True)

    class Meta:

        permissions = [
            ("change_discount", "Can modify a Pedido discount"),
        ]

        ordering = ["-fecha_entrega", "-modified"]

    def __str__(self) -> str:
        return f"Pedido #{self.id}"

    def get_absolute_url(self) -> str:
        """ Utilizada después de actualizar o eliminar un pedido"""
        return reverse("pedidos:detail", kwargs={"pk": self.id})

    def save(self, *args, **kwargs):
        """
        Cuando se guarde un pedido con estado `En Proceso`
        se crea o actualiza la OT correspondiente.
        """

        super().save(*args, **kwargs)

        if self.estado == Pedido.EN_PROCESO:
            # Si cambia el pedido -> Actualizar OT
            # Si no existe -> Crear OT
            orden_trabajo, created = OrdenTrabajo.objects.update_or_create(pedido=self,)

    @property
    def tiempo_total(self) -> int:
        """ Devuelve la sumatoria de tiempo para producir todos los productos del pedido """
        return sum(producto.tiempo for producto in self.productos_pedido.all())

    @property
    def get_precio_total(self) -> float:
        """ Devuelve el precio total del pedido """
        return sum(producto.precio_pedido for producto in self.productos_pedidos.all())

    def save_precio_total(self) -> None:
        """ Guarda el precio total del pedido """
        self.precio_total = sum(
            producto.precio_pedido for producto in self.productos_pedidos.all()
        )
        self.save()

    def cambiar_estado(self, nuevo_estado: int) -> None:
        """ Cambia el estado del pedido  """
        self.estado = nuevo_estado
        self.save()


class ProductosPedido(BaseModel):

    # Si se elimina un Pedido, se eliminan los datos asociados a éste
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, related_name="productos_pedidos"
    )

    # Si se elimina un Producto, sólo se quitara el registro
    # de ese producto del pedido.
    producto = models.ForeignKey("productos.Producto", on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Productos Pedidos"

    def __str__(self) -> str:
        return f"{self.cantidad} - {self.producto.nombre}"

    @property
    def precio_pedido(self) -> float:
        """ Calcula el precio total de cada producto del pedido """
        return self.cantidad * self.producto.get_precio()


class OrdenTrabajo(BaseModel):

    INICIADA = 0
    FINALIZADA = 1

    ESTADO_ORDEN_TRABAJO_CHOICES = (
        (INICIADA, "Iniciada"),
        (FINALIZADA, "Finalizada"),
    )

    # Borrar OT si se borra el pedido asociado
    pedido = models.OneToOneField(
        Pedido, on_delete=models.CASCADE, related_name="orden_de_trabajo"
    )
    estado = models.IntegerField(default=INICIADA, choices=ESTADO_ORDEN_TRABAJO_CHOICES)

    detalles = models.TextField(blank=True)

    class Meta:
        verbose_name = "Orden de Trabajo"
        verbose_name_plural = "Órdenes de Trabajo"

    def __str__(self) -> str:
        """Unicode representation of OrdenTrabajo."""
        return f"Orden de trabajo #{self.id}"

    def get_absolute_url(self):
        """Return absolute url for OrdenTrabajo."""
        return reverse("pedidos:ot_detail", kwargs={"pk": self.id})

    def finalizar_orden_trabajo(self) -> None:
        """
        Cambia el estado de:
        Orden de Trabajo => Finalizada
        Pedido => Listo para entrega
        """

        self.estado = OrdenTrabajo.FINALIZADA
        self.pedido.estado = Pedido.LISTO

        self.pedido.save()

        self.save()
