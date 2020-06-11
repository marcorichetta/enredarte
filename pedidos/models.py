from django.db import models
from django.urls import reverse

# Create your models here.


class Pedido(models.Model):

    CREADO = 1
    EN_PROCESO = 2
    ENTREGADO = 3
    PAGADO = 4

    ESTADO_PEDIDO_CHOICES = (
        (CREADO, 'Creado'),
        (EN_PROCESO, 'En proceso'),
        (ENTREGADO, 'Entregado'),
        (PAGADO, 'Pagado'),
    )

    # Un cliente no se puede eliminar si tiene pedidos asociados
    cliente = models.ForeignKey(
        "clientes.Cliente", on_delete=models.PROTECT, related_name="clientes")
    productos_pedido = models.ManyToManyField(
        'productos.Producto', through="ProductosPedido")
    precio_final = models.DecimalField(
        help_text='Precio en $', max_digits=6, decimal_places=2)
    detalles = models.TextField(blank=True)
    estado = models.IntegerField(default=CREADO, choices=ESTADO_PEDIDO_CHOICES)
    actualizado = models.DateTimeField(
        auto_now=True, help_text="Última vez actualizado")
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField(verbose_name="Fecha de entrega estimada")

    def __str__(self):
        return f"Pedido #{self.id}"

    class Meta:
        ordering = ['-fecha_pedido', '-actualizado']

    def get_absolute_url(self):
        """ Utilizada después de actualizar o eliminar un pedido"""
        return reverse('pedido')
        
        # return reverse('detailPedido', kwargs={'pk': self.id})

    @property
    def get_productos(self):
        ''' Devuelve los productos relacionados a este pedido '''
        productos = Pedido.objects.get(id=self.id).productos_pedido.all()

        return productos

    def get_status(self):
        if self.estado == "pagado":
            return "Pedido pagado"
        elif self.estado == "entregado":
            return "Pedido entregado"
        return "En proceso"


class ProductosPedido(models.Model):
    
    # Si se elimina un Pedido, se eliminan los datos asociados a éste
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    # Si se elimina un Producto, sólo se quitara el registro 
    # de ese producto del pedido.
    producto = models.ForeignKey(
        'productos.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} - {self.producto.nombre}"
