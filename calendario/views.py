from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse

from pedidos.models import Pedido

class Calendario(LoginRequiredMixin, TemplateView):
    """ View que contiene un calendario interactivo con pedidos """

    template_name = "calendario/calendario.html"

    def get_context_data(self, **kwargs):
        context = super(Calendario, self).get_context_data(**kwargs)
        context["estados_pedidos"] = {
            'Creado' : Pedido.CREADO,
            'En Proceso' : Pedido.EN_PROCESO,
            'Entregado' : Pedido.ENTREGADO,
            'Pagado' : Pedido.PAGADO,
        }

        return context

@require_http_methods(["GET"])
def get_pedidos(request:HttpRequest, idEstado: int == 9) -> JsonResponse:
    """ Función llamada mediante AJAX que devuelve pedidos

        :param idEstado: ID del estado sobre el que se quiere filtrar

        :returns: Pedidos filtrados en base al estado. Últimos 50 pedidos en general.
    """

    #TODO Esto se debe poder hacer de una forma más funcional
    if idEstado == 9:
        pedidos = Pedido.objects.all()[:50]
    else:
        pedidos = Pedido.objects.filter(estado=idEstado)

    pedidos = [{
        'id': p.pk,
        'title': str(p.cliente),
        'start': p.fecha_pedido.isoformat(),
        'status': p.estado,
    } for p in pedidos]

    return JsonResponse(pedidos, safe=False)