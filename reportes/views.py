from core.models import Localidad
from django.db.models import Count
from django.http import JsonResponse
from django.views.generic import TemplateView
from pedidos.models import Pedido

import datetime


class ReportesView(TemplateView):
    template_name = "reportes/listado.html"


class ClientesLocalidadView(TemplateView):
    template_name = "reportes/clientes-localidad.html"


class PedidosTiempoView(TemplateView):
    template_name = "reportes/pedidos-tiempo.html"


class ProductosMasSolicitadosView(TemplateView):
    template_name = "reportes/productos-solicitados.html"


def productos_mas_solicitados(request):

    # Recorrer los pedidos
    # Por cada pedido extraer los productos y sus cantidades
    # Mezclar los productos y sumar las cantidades
    # Obtener un dict con los productos junto a sus cantidades
    # Ordenar por producto

    pedidos = Pedido.objects.all()

    [produ.cantidad for produ in p.productos_pedidos.all() for p in pedidos]

    data = []

    return JsonResponse()


def pedidos_por_tiempo(request):

    # labels = []
    data = []

    fecha_inicio = datetime.date(2020, 6, 1)
    fecha_final = datetime.date(2020, 12, 31)

    jul = Pedido.objects.filter(fecha_pedido__month="7").count()
    ago = Pedido.objects.filter(fecha_pedido__month="8").count()
    sept = Pedido.objects.filter(fecha_pedido__month="9").count()
    octu = Pedido.objects.filter(fecha_pedido__month="10").count()
    nov = Pedido.objects.filter(fecha_pedido__month="11").count()
    dec = Pedido.objects.filter(fecha_pedido__month="12").count()

    # qs = Pedido.objects.filter(fecha_pedido__gte=fecha_inicio, fecha_pedido__lte=fecha_final).values("fecha_pedido",)

    data = [jul, ago, sept, octu, nov, dec]

    return JsonResponse(data={"pedidos": data})


def cliente_por_localidad(request):

    labels = []
    data = []

    qs = (
        Localidad.objects.values("localidad")
        .annotate(num_clientes=Count("clientes"))
        .exclude(num_clientes__lte=0)
    )

    for c in qs:
        labels.append(c["localidad"])
        data.append(c["num_clientes"])

    return JsonResponse(data={"labels": labels, "num_clientes": data})
