from django.test import TestCase
import pytest

from pedidos.forms import PedidoForm, ProductosPedidoFormset
from productos.tests.factories import ProductoFactory
from clientes.tests.factories import ClienteFactory
from pedidos.tests.factories import PedidoFactory

from core.utils import build_formset_data


@pytest.mark.django_db
class Test_Form_Pedido:
    def test_form_pedido(self):

        cliente = ClienteFactory()

        data = {
            "cliente": cliente.pk,
            "estado": 0,
            "fecha_entrega": "06/08/2020",
            "descuento": 0,
        }

        form = PedidoForm(data=data)

        assert form.is_valid()
