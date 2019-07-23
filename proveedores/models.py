from django.db import models
from django.urls import reverse
from .helpers import validar_cuit

# Create your models here.


class Proveedor(models.Model):
    cuit = models.CharField(max_length=13, unique=True,
                            validators=[validar_cuit],
                            help_text="Ingrese el CUIT con el siguiente formato: 20-12345678-9")
    razon_social = models.CharField(max_length=64)
    telefono = models.CharField(max_length=64)
    email = models.EmailField()
    calle = models.CharField(max_length=64)
    numero = models.CharField(max_length=4)
    localidad = models.ForeignKey(
        'gestion.Localidad', on_delete=models.CASCADE, related_name='proveedores')
    detalles = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"{self.razon_social}"

    def get_absolute_url(self):
        return reverse('proveedor')