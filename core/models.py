from django.db import models

# Create your models here.


class Provincia(models.Model):
    cod_provincia = models.CharField(max_length=10, blank=False, default="AR-")
    provincia = models.CharField(max_length=50, blank=False, default="Provincia")

    class Meta:
        ordering = ["provincia"]

    def __str__(self):
        return f"{self.provincia}"


class Localidad(models.Model):
    cod_postal = models.CharField(max_length=10)
    localidad = models.CharField(max_length=128)
    # Una provincia no se puede eliminar si tiene localidades asociadas
    provincia = models.ForeignKey(
        Provincia, on_delete=models.PROTECT, related_name="provincias"
    )

    class Meta:
        verbose_name_plural = "Localidades"
        ordering = ["localidad"]

    def __str__(self):
        return self.localidad
