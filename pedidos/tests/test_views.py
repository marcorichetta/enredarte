from django.test import TestCase
from django import urls
import pytest

from pedidos.forms import PedidoForm, ProductosPedidoFormset
from productos.tests.factories import ProductoFactory
from clientes.tests.factories import ClienteFactory
from pedidos.tests.factories import PedidoFactory

from core.utils import build_formset_data


@pytest.fixture
def form_pedido(self):

    cliente = ClienteFactory()

    data = {
        "cliente": str(cliente.pk),
        "detalles": "123",
        "estado": "0",
        "fecha_entrega": "06/08/2020",
    }

    form = PedidoForm(data=data)

    return form


@pytest.mark.django_db
class Test_Nuevo_Pedido:
    def test_crear_pedido(self, django_db_setup, form_pedido):

        nuevo_pedido = form_pedido.save()

        assert form_pedido.is_valid()

        assert nuevo_pedido.get_precio_total == 100
        assert nuevo_pedido.precio_total == 100

    def test_pedido_con_formset(self, django_db_setup, form_pedido):

        producto1 = ProductoFactory()
        producto2 = ProductoFactory()

        forms = [
            {
                "id": "",
                "pedido": "",
                "producto": producto1.pk,
                "cantidad": 5,
                "DELETE": "",
            },
            {"id": 1, "producto": producto2.pk, "cantidad": 3},
        ]

        formset_data = build_formset_data(prefix="productos_pedidos", forms=forms)

        my_data = {**data, **formset_data}

        assert final_data == my_data

        pp_formset = ProductosPedidoFormset(data=final_data)

        assert pp_formset.is_valid()
