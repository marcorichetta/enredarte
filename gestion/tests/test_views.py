import pytest, json

# Tests para views de Localidad y Provincia

from gestion.models import Localidad, Provincia
from utiles.factories import ProvinciaFactory, LocalidadFactory


@pytest.mark.django_db
def test_ajax_request_nueva_localidad(client):
    """ Crea una nueva localidad simulando la request del modal de la ruta clientes/new"""

    # Creamos la data necesaria para realizar los tests
    provincia1 = ProvinciaFactory()

    testData = {"cod_postal": "9999", "localidad": "Test", "provincia_id": provincia1.id}

    response = client.post("/localidad/new/", testData)

    # Obtener la localidad creada
    localidadCreada = Localidad.objects.get(id=1)

    valoresEsperados = ["9999", "Test", 1]

    valoresEnDB = [
        localidadCreada.cod_postal,
        localidadCreada.localidad,
        localidadCreada.provincia_id,
    ]

    assert valoresEnDB == valoresEsperados
