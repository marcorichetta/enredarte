# Unit tests para el modelo Cliente
import pytest
from clientes.tests.factories import ClienteFactory
from clientes.models import Cliente


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
