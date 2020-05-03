import pytest

# Tests para views de Localidad y Provincia

from gestion.models import Localidad
from utiles.factories import ProvinciaFactory, LocalidadFactory


@pytest.fixture
@pytest.mark.django_db
def test_data(client):

    # Creamos la data necesaria para realizar los tests
    # provincia1 = ProvinciaFactory()

    testData = {"cod_postal": "9999", "localidad": "Test", "provincia_id": 1}

    response = client.post("/localidad/new/", testData)

    return response


def test_ajax_request(django_db_setup, test_data):
    """ Crea una nueva localidad simulando la request del modal de la ruta clientes/new"""

    assert test_data.status_code == 200


@pytest.mark.django_db
def test_nueva_localidad(django_db_setup):

    # Obtener la localidad creada
    localidadCreada = Localidad.objects.get(id=1)

    valoresEsperados = ["9999", "Test", 1]

    valoresEnDB = [
        localidadCreada.cod_postal,
        localidadCreada.localidad,
        localidadCreada.provincia_id,
    ]

    assert valoresEnDB == valoresEsperados
