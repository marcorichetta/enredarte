from django.db import models
from core.base_model import BaseModel


class Variable(BaseModel):
    """
        Variables globales utilizadas por el sistema para el calculo de precios

        Se crean al inicializar el proyecto mediante el comando
        `crear_variables.py` ubicado en managements/commands

    """

    precio_hora = models.DecimalField(
        help_text="Precio de la hora de trabajo",
        max_digits=5,
        decimal_places=2,
        blank=True,
    )

    precio_pintado = models.DecimalField(
        help_text="Precio de la pintura/apliques incluídos en el producto",
        max_digits=5,
        decimal_places=2,
        blank=True,
    )

    ganancia_por_mayor = models.DecimalField(
        help_text="Porcentaje de ganancia por mayor",
        max_digits=5,
        decimal_places=2,
        blank=True,
    )

    ganancia_por_menor = models.DecimalField(
        help_text="Porcentaje de ganancia por menor",
        max_digits=5,
        decimal_places=2,
        blank=True,
    )

    ganancia_fibrofacil = models.DecimalField(
        help_text="Porcentaje de ganancia aplicada al fibrofacil",
        max_digits=5,
        decimal_places=2,
        blank=True,
    )

    def __str__(self):
        return f"\
            Ganancia por mayor: {self.ganancia_por_mayor}% \n\
            Ganancia por menor: {self.ganancia_por_menor}% \n\
            Ganancia_fibrofacil: {self.ganancia_fibrofacil}% \n\
            Precio de hora: ${self.precio_hora}\n\
            Precio de pintado: ${self.precio_pintado}"

    @property
    def get_ganancias(self):
        """ Devuelve una lista con las ganancias """
        return [self.ganancia_por_mayor, self.ganancia_por_menor]
