from django.db import models
from core.base_model import BaseModel


class Variable(BaseModel):
    precio_hora = models.PositiveSmallIntegerField(
        help_text="Precio de la hora de trabajo", blank=True
    )

    precio_pintado = models.PositiveSmallIntegerField(
        help_text="Precio de la pintura/apliques incluídos en el producto", blank=True
    )

    ganancia_por_mayor = models.PositiveSmallIntegerField(
        help_text="Porcentaje de ganancia por mayor", blank=True
    )

    ganancia_por_menor = models.PositiveSmallIntegerField(
        help_text="Porcentaje de ganancia por menor", blank=True
    )

    ganancia_fibrofacil = models.PositiveSmallIntegerField(
        help_text="Porcentaje de ganancia aplicada al fibrofacil", blank=True
    )

    def __str__(self):
        return f"\
            Ganancia por mayor: {self.ganancia_por_mayor}% \n\
            Ganancia por menor: {self.ganancia_por_menor}% \n\
            Precio de hora: ${self.precio_hora}\n\
            Precio de pintado: ${self.precio_pintado}"

    @property
    def get_ganancias(self):
        """ Devuelve una lista con las ganancias """
        return [self.ganancia_por_mayor, self.ganancia_por_menor]

    @property
    def get_ganancia_ff(self):
        return self.ganancia_fibrofacil

    @property
    def get_precio_pintado(self):
        return self.precio_pintado

    @property
    def get_precio_hora(self):
        return self.precio_hora
