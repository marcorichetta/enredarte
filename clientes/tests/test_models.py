import pytest
from pytest_django.asserts import TestCase

# Unit tests para el modelo Cliente

from clientes.models import Cliente
from gestion.models import Localidad, Provincia

from utiles.factories import ProvinciaFactory, LocalidadFactory


@pytest.mark.django_db
def test_crear_cliente():

    # Creamos la data necesaria para realizar los tests
    locTest = LocalidadFactory()

    Cliente.objects.create(
        nombre="Marco",
        apellido="Richetta",
        email="marcorichetta@gmail.com",
        telefono="3534123456",
        calle="Santa Fe",
        numero="565",
        localidad=locTest,
    )

    def test_creacion_correcta():
        cliente = Cliente.objects.get(id=1)

        assert isinstance(cliente, Cliente)

    def test_get_absolute_url():
        """ El método get_absolute_url debe dirigir a la página inicial de Clientes """

        cliente = Cliente.objects.get(id=1)

        assert cliente.get_absolute_url() == "/clientes/"
