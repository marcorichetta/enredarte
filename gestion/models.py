from django.db import models
from django.urls import reverse

# Create your models here.



class Provincia(models.Model):
    cod_provincia = models.CharField(max_length=10, blank=False, default='AR-')
    provincia = models.CharField(
        max_length=50, blank=False, default='Provincia')

    class Meta:
        ordering = ['provincia']

    def __str__(self):
        return f"{self.provincia}"


class Localidad(models.Model):
    cod_postal = models.CharField(max_length=10)
    localidad = models.CharField(max_length=128)
    provincia = models.ForeignKey(
        Provincia, on_delete=models.CASCADE, related_name='provincias')

    class Meta:
        verbose_name_plural = 'Localidades'
        ordering = ['localidad']

    def __str__(self):
        return self.localidad


""" class Pedido(models.Model):
    fecha_pedido = models.DateField(auto_now_add=True)
    cliente = models.OneToOneField("clientes.Cliente", on_delete=models.CASCADE)
    productos_pedido = models.ManyToManyField('productos.Producto')
    precio_final = models.DecimalField(
        help_text='Precio en $', max_digits=6, decimal_places=2)
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"Pedido #{self.id}" """