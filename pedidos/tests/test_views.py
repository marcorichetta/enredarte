import pytest
from clientes.tests.factories import ClienteFactory
from django.template.defaultfilters import floatformat
from django.test import RequestFactory
from pedidos.forms import PedidoForm, ProductosPedidoFormset
from pedidos.models import Pedido
from pedidos.tests.factories import PedidoFactory
from productos.models import Producto
from productos.tests.factories import InsumoFactory, ProductoFactory
from users.tests.factories import CustomUserFactory
from variables.models import Variable
from django.urls import reverse
from pedidos.views import PedidoCreateView


@pytest.fixture
def productos():

    Variable.objects.create(
        precio_hora=40,
        precio_pintado=50,
        ganancia_por_mayor=45,
        ganancia_por_menor=55,
        ganancia_fibrofacil=15,
    )

    insumo1 = InsumoFactory(precio=100)
    insumo2 = InsumoFactory(precio=200)

    producto1 = ProductoFactory(
        largo=10, ancho=20, alto=4, tiempo=35, insumo_base=insumo1, insumo_lados=insumo2
    )
    producto2 = ProductoFactory(
        largo=20, ancho=30, alto=5, tiempo=45, insumo_base=insumo1, insumo_lados=insumo2
    )

    return [producto1, producto2]


@pytest.fixture
def form_pedido():

    cliente = ClienteFactory()

    data = {
        "cliente": str(cliente.pk),
        "detalles": "123",
        "estado": "0",
        "fecha_entrega": "06/08/2020",
        "descuento": 0,
    }

    form = PedidoForm(data=data)

    return form


@pytest.mark.django_db
class Test_Nuevo_Pedido:
    def test_pedido_con_formset(self, django_db_setup, form_pedido, productos):
        """ Crear un Pedido con productos (form y formset) y calcular su precio """

        # forms = [
        #     {
        #         "pedido": "",
        #         "producto": producto1.pk,
        #         "cantidad": 3,
        #     },
        #     {
        #         "pedido": "",
        #         "producto": producto2.pk,
        #         "cantidad": 5,
        #     },
        # ]

        # formset_data = build_formset_data(prefix="productos_pedidos", forms=forms)

        # final_data2 = {
        #     "cliente": "1",
        #     "detalles": "123",
        #     "estado": "0",
        #     "fecha_entrega": "06/08/2020",
        #     **formset_data
        # }

        final_data = {
            "cliente": "1",
            "detalles": "123",
            "estado": "0",
            "fecha_entrega": "06/08/2020",
            "productos_pedidos-TOTAL_FORMS": 2,
            "productos_pedidos-INITIAL_FORMS": 0,
            "productos_pedidos-MIN_NUM_FORMS": 1,
            "productos_pedidos-MAX_NUM_FORMS": 5,
            "productos_pedidos-0-id": "",
            "productos_pedidos-0-pedido": "",
            "productos_pedidos-0-producto": productos[0].pk,
            "productos_pedidos-0-cantidad": 5,
            "productos_pedidos-0-DELETE": "",
            "productos_pedidos-1-producto": productos[1].pk,
            "productos_pedidos-1-cantidad": 3,
        }

        # Guardar el formulario
        nuevo_pedido = form_pedido.save()

        pp_formset = ProductosPedidoFormset(data=final_data)
        assert pp_formset.is_valid()

        pp_formset.instance = nuevo_pedido
        pp_formset.save()

        assert round(nuevo_pedido.get_precio_total) == 1701

    def test_pedido_actualizado(self, django_db_setup, productos):
        """ Si se actualiza un pedido con nuevos productos el precio total cambia """

        # Crear el pedido
        pedido: Pedido = PedidoFactory()

        # Estos productos son creados con el fixture `productos`
        prods = Producto.objects.all()[:2]

        # Agregar los productos a través de la tabla relacional
        # especificando 2 de cada uno
        pedido.productos_pedido.add(*prods, through_defaults={"cantidad": 2})

        assert (
            floatformat(pedido.get_precio_total) == "873,3"
        ), "El precio del pedido no coincide con el esperado"


@pytest.mark.skip()
def test_usuario_registrado_en_pedido(db):
    factory = RequestFactory()
    user = CustomUserFactory()
    cliente = ClienteFactory()
    producto = ProductoFactory()

    data = {
        "cliente": str(cliente.pk),
        "detalles": "123",
        "estado": "0",
        "fecha_entrega": "06/08/2020",
        "productos_pedidos-TOTAL_FORMS": 1,
        "productos_pedidos-INITIAL_FORMS": 0,
        "productos_pedidos-MIN_NUM_FORMS": 1,
        "productos_pedidos-MAX_NUM_FORMS": 5,
        "productos_pedidos-0-producto": producto.pk,
        "productos_pedidos-0-cantidad": 3,
    }

    request = factory.post(reverse("pedidos:create"), data)
    request.user = user

    response = PedidoCreateView.as_view()(request)

    assert response.status_code == 200
    assert Pedido.objects.count() == 1
