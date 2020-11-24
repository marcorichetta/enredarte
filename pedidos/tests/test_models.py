import pytest
from pedidos.tests.factories import PedidoFactory
from pedidos.models import OrdenTrabajo, Pedido


@pytest.mark.django_db
def test_orden_trabajo_creada_al_pagar():
    """
    GIVEN Pedido creado
    WHEN Pedido.estado => Pagado
    THEN Se crea OrdenTrabajo asociada al Pedido
    """

    pedido = PedidoFactory()

    pedido.estado = Pedido.PAGADO
    pedido.save()

    assert OrdenTrabajo.objects.count() == 1
