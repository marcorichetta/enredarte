import pytest

# Unit tests para el modelo Cliente

from clientes.models import Cliente

from utiles.factories import ProvinciaFactory, LocalidadFactory


@pytest.fixture
def crear_cliente():

    # Creamos la data necesaria para realizar los tests
    locTest = LocalidadFactory()

    clienteTest = Cliente.objects.create(
        nombre="Marco",
        apellido="Richetta",
        email="marcorichetta@gmail.com",
        telefono="3534123456",
        calle="Santa Fe",
        numero="565",
        localidad=locTest,
    )

    return clienteTest


@pytest.mark.django_db()
def test_reverse(django_db_setup, crear_cliente):

    # cliente = Cliente.objects.get(id=1)

    assert crear_cliente.get_absolute_url() == "/clientes/"
