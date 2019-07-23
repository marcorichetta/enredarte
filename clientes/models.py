from django.db import models
from django.urls import reverse

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    email = models.EmailField()
    telefono = models.CharField(max_length=64)
    calle = models.CharField(max_length=64)
    numero = models.CharField(max_length=6)
    localidad = models.ForeignKey(
        "gestion.Localidad", on_delete=models.CASCADE, related_name='clientes')
    detalles = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre', 'apellido']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_email(self):
        return self.email

    def get_absolute_url(self):
        return reverse('cliente')