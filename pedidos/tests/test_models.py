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

    pedido.estado = Pedido.EN_PROCESO
    pedido.save()

    assert OrdenTrabajo.objects.count() == 1


@pytest.mark.django_db
def test_pedido_listo_al_finalizar_orden_trabajo():
    """
    GIVEN Pedido `En Proceso` y OrdenTrabajo `Iniciada`
    WHEN OrdenTrabajo.estado => `Finalizada`
    THEN Se cambia el estado del Pedido a `Listo`
    """

    # Pedido En Proceso crea la Orden de Trabajo correspondiente
    pedido = PedidoFactory(estado=Pedido.EN_PROCESO)

    assert pedido.estado == Pedido.EN_PROCESO
    assert OrdenTrabajo.objects.count() == 1

    assert pedido.orden_de_trabajo.estado == OrdenTrabajo.INICIADA

    pedido.orden_de_trabajo.finalizar_orden_trabajo()

    assert pedido.estado == Pedido.LISTO
    assert pedido.orden_de_trabajo.estado == OrdenTrabajo.FINALIZADA
