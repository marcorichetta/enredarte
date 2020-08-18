from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class BaseModel(SoftDeletableModel, TimeStampedModel, models.Model):
    """
        Modelo base para todos los modelos del proyecto.

        SoftDeletableModel: Sobreescribe el método `delete` del modelo
        y sólo cambia el campo `is_removed` a `True`. Además provee un `manager` que filtra los objetos borrados.

        TimeStampedModel: Provee los campos `created` y `modified` que son actualizados automáticamente.

        Más info: https://django-model-utils.readthedocs.io/en/latest/models.html
    """

    class Meta:
        abstract = True
