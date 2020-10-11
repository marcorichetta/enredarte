# Unit tests para el modelo Cliente
import pytest
from clientes.tests.factories import ClienteFactory
from clientes.models import Cliente
from django.db import IntegrityError


@pytest.fixture
def cliente():
    # Fixture para crear el cliente necesario para los tests

    cliente = ClienteFactory()

    return cliente


@pytest.mark.django_db()
class TestClientes:
    def test_creado_borrado_cliente(self, cliente):

        assert Cliente.all_objects.count() == 1

        cliente.delete()

        # El manager `objects` devuelve sólo las instancias activas
        assert Cliente.objects.count() == 0
        # El manager `all_objects` devuelve todas las instancias creadas
        assert Cliente.all_objects.count() == 1

    def test_reverse(self, cliente):

        assert cliente.get_absolute_url() == "/clientes/1/"


@pytest.mark.django_db()
def test_soft_delete_no_deja_crear_en_BD_unique_key():
    """ Crear cliente con mismo CUIT que un registro existente da error de integridad """

    cliente = ClienteFactory(nombre="Cliente", apellido="1", cuit="30-52999943-3")

    assert Cliente.all_objects.count() == 1

    cliente.delete()

    # El manager `objects` devuelve sólo las instancias activas
    assert Cliente.objects.count() == 0
    # El manager `all_objects` devuelve todas las instancias creadas
    assert Cliente.all_objects.count() == 1

    # Nuevo cliente con mismo cuit (Unique key) da error de integridad
    with pytest.raises(IntegrityError):
        cliente = ClienteFactory(nombre="Cliente", apellido="2", cuit="30-52999943-3")


@pytest.mark.django_db()
def test_Cliente_se_puede_restaurar():
    """ Cliente borrado lógicamente se puede restaurar """

    client = ClienteFactory(nombre="Cliente", apellido="1")

    client.delete()

    assert client.is_removed is True
    assert Cliente.objects.count() == 0
    assert Cliente.all_objects.count() == 1

    client.is_removed = False
    client.save()

    assert Cliente.objects.count() == 1
