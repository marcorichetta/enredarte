from django.db import models
from django.urls import reverse

# Create your models here.

class Pedido(models.Model):

    ESTADO_PEDIDO_CHOICES = (
        ('creado', 'Creado'),    
        ('pagado', 'Pagado'),
        ('enviado', 'Enviado'),
    )

    cliente = models.ForeignKey("clientes.Cliente", on_delete=models.CASCADE)
    productos_pedido = models.ManyToManyField('productos.Producto')
    precio_final = models.DecimalField(
        help_text='Precio en $', max_digits=6, decimal_places=2)
    detalles = models.TextField(blank=True)
    estado = models.CharField(max_length=64, default='creado', choices=ESTADO_PEDIDO_CHOICES)
    actualizado = models.DateTimeField(auto_now=True)
    fecha_pedido = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id}"
    
    class Meta:
        ordering = ['-fecha_pedido', '-actualizado']

    """ def get_absolute_url(self):
        return reverse("orders:detail", kwargs={'order_id': self.order_id}) """

    def get_status(self):
        if self.estado == "pagado":
            return "Pedido pagado"
        elif self.estado == "enviado":
            return "Pedido enviado"
        return "En proceso"
