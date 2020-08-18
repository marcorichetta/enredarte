import pytest
from django.urls import reverse

# Tests para views de Localidad y Provincia

from core.models import Localidad
from django.shortcuts import get_object_or_404
from .factories import ProvinciaFactory, LocalidadFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def nueva_localidad(client):
    # Fixture para crear el cliente necesario para los tests

    provincia = ProvinciaFactory()

    # localidad = LocalidadFactoryFactory()
    url = reverse("crearLocalidad")

    testData = {"cod_postal": "9999", "localidad": "Test", "provincia_id": provincia.pk}

    response = client.post(url, data=testData)

    return response


@pytest.mark.django_db()
def test_ajax_request(nueva_localidad):
    """ Crea una nueva localidad simulando la request del modal de la ruta clientes/new"""

    assert nueva_localidad.status_code == 200


@pytest.mark.django_db()
def test_nueva_localidad(nueva_localidad):

    # Obtener la localidad creada
    localidadCreada = get_object_or_404(Localidad, id=1)

    valoresEsperados = ["9999", "Test", 1]

    valoresEnDB = [
        localidadCreada.cod_postal,
        localidadCreada.localidad,
        localidadCreada.provincia_id,
    ]

    assert valoresEnDB == valoresEsperados
