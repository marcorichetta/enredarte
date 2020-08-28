from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from datetime import date

from core.base_model import BaseModel
from productos.models import Producto


class Pedido(BaseModel):

    CREADO = 0
    EN_PROCESO = 1
    ENTREGADO = 2
    PAGADO = 3

    ESTADO_PEDIDO_CHOICES = (
        (CREADO, "Creado"),
        (EN_PROCESO, "En proceso"),
        (ENTREGADO, "Entregado"),
        (PAGADO, "Pagado"),
    )

    # Un cliente no se puede eliminar si tiene pedidos asociados
    cliente = models.ForeignKey(
        "clientes.Cliente", on_delete=models.PROTECT, related_name="clientes"
    )
    productos_pedido = models.ManyToManyField(
        "productos.Producto", through="ProductosPedido"
    )
    precio_total = models.DecimalField(
        help_text="Precio en $", max_digits=6, decimal_places=2
    )
    detalles = models.TextField(blank=True)
    estado = models.IntegerField(default=CREADO, choices=ESTADO_PEDIDO_CHOICES)
    fecha_pedido = models.DateField(default=date.today, verbose_name="Fecha de pedido")
    fecha_entrega = models.DateField(verbose_name="Fecha de entrega estimada", blank=True)

    def __str__(self) -> str:
        return f"Pedido #{self.id}"

    class Meta:
        ordering = ["-fecha_entrega", "-modified"]

    def get_absolute_url(self) -> str:
        """ Utilizada después de actualizar o eliminar un pedido"""
        return reverse("detailPedido", kwargs={"pk": self.id})

    @property
    def tiempo_total(self) -> int:
        """ Devuelve la sumatoria de tiempo para producir todos los productos del pedido """
        return sum(producto.tiempo for producto in self.productos_pedido.all())

    @property
    def get_precio_total(self) -> int:
        """ Devuelve el precio total del pedido """
        return sum(producto.precio_pedido for producto in self.productos_pedidos.all())

    def save_precio_total(self) -> None:
        """ Devuelve el precio total del pedido """
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

    def __str__(self) -> str:
        return f"{self.cantidad} - {self.producto.nombre}"

    @property
    def precio_pedido(self):
        """ Calcula el precio total de cada producto del pedido """
        return self.cantidad * self.producto.precio_venta_terminado
