from pedidos.models import OrdenTrabajo, Pedido
from django.http import HttpResponseRedirect
from django.contrib import messages


# TODO - #50 Agregar cambio de estado Listo => Entregado
def PedidoEnProcesoView(request):
    """
    Endpoint para cambiar el estado del pedido a En Proceso.
    Redirige a la misma página de la que vino
    """

    pedido_id = request.POST.get("id_pedido")
    estado_pedido = request.POST.get("estado_pedido")

    pedido_a_cambiar: Pedido = Pedido.objects.get(id=pedido_id)

    if int(estado_pedido) == Pedido.CREADO:
        pedido_a_cambiar.estado = Pedido.EN_PROCESO
        pedido_a_cambiar.save()

        messages.success(request, f"El {pedido_a_cambiar} se cambió a estado: En Proceso")
        messages.success(request, "Se creó la Orden de Trabajo correspondiente")
    else:
        pedido_a_cambiar.estado = Pedido.ENTREGADO
        pedido_a_cambiar.save()

        messages.success(request, f"El {pedido_a_cambiar} se cambió a estado: Entregado")

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def OrdenTrabajoFinalizadaView(request):
    """
    Endpoint para cambiar el estado de una Orden de Trabajo a Finalizada.
    A su vez el Pedido asociado a la OT se cambiará a estado Listo para Entrega
    """

    orden_trabajo_id = request.POST.get("id_orden_trabajo")

    ot_a_finalizar: OrdenTrabajo = OrdenTrabajo.objects.get(id=orden_trabajo_id)

    ot_a_finalizar.finalizar_orden_trabajo()

    messages.success(request, f"La {ot_a_finalizar} se cambió a estado: Finalizada")
    messages.success(
        request, f"El {ot_a_finalizar.pedido} se encuentra Listo para Entrega"
    )

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
