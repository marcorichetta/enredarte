import pytest

# Tests para views de Localidad y Provincia

from core.models import Localidad
from django.shortcuts import get_object_or_404
from utiles.factories import ProvinciaFactory, LocalidadFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def test_data(client):

    # Creamos la data necesaria para realizar los tests
    # provincia1 = ProvinciaFactory()

    testData = {"cod_postal": "9999", "localidad": "Test", "provincia_id": 1}

    response = client.post("/localidad/new/", testData)

    return response


def test_ajax_request(django_db_setup, test_data):
    """ Crea una nueva localidad simulando la request del modal de la ruta clientes/new"""

    assert test_data.status_code == 200


def test_nueva_localidad(django_db_setup, test_data):

    # Obtener la localidad creada
    localidadCreada = get_object_or_404(Localidad, id=1)

    valoresEsperados = ["9999", "Test", 1]

    valoresEnDB = [
        localidadCreada.cod_postal,
        localidadCreada.localidad,
        localidadCreada.provincia_id,
    ]

    print(valoresEnDB)

    assert valoresEnDB == valoresEsperados
