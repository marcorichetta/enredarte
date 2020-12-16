from core.models import Localidad
from django.db.models import Count
from django.http import JsonResponse
from django.views.generic import TemplateView
from pedidos.models import Pedido, ProductosPedido

import datetime
from clientes.models import Cliente

meses = [
    "_",
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]


class ReportesView(TemplateView):
    template_name = "reportes/listado.html"


class ClientesLocalidadView(TemplateView):
    template_name = "reportes/clientes-localidad.html"


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


class PedidosTiempoView(TemplateView):
    template_name = "reportes/pedidos-tiempo.html"


def pedidos_por_tiempo(request):

    str_fecha_inicio = request.GET.get("fecha_inicio") or "2020-6-1"
    str_fecha_fin = request.GET.get("fecha_fin") or "2020-12-1"

    inicio = datetime.datetime.strptime(str_fecha_inicio, "%Y-%m-%d")
    fin = datetime.datetime.strptime(str_fecha_fin, "%Y-%m-%d")

    qs = (
        Pedido.objects.filter(fecha_pedido__gte=inicio, fecha_pedido__lte=fin)
        .values_list("fecha_pedido__month")
        .annotate(num=Count("pk"))
        .order_by("fecha_pedido__month")
    )

    labels = [meses[reg[0]] for reg in qs]  # reg[0] == 1, 2, 3...
    data = [reg[1] for reg in qs]

    return JsonResponse(data={"meses": labels, "num_pedidos": data})


class ProductosMasSolicitadosView(TemplateView):
    template_name = "reportes/productos-solicitados.html"


def productos_mas_solicitados(request):
    """ Productos más pedidos ordenados de mayor a menor """

    str_fecha_inicio = request.GET.get("fecha_inicio") or "2020-6-1"
    str_fecha_fin = request.GET.get("fecha_fin") or "2020-12-1"

    inicio = datetime.datetime.strptime(str_fecha_inicio, "%Y-%m-%d")
    fin = datetime.datetime.strptime(str_fecha_fin, "%Y-%m-%d")

    qs = (
        ProductosPedido.objects.filter(
            pedido__fecha_pedido__gte=inicio, pedido__fecha_pedido__lte=fin
        )
        .values_list("producto__nombre")
        .annotate(num_productos=Count("cantidad"))
        .order_by("num_productos")
    )

    # labels = [meses[reg[0]] for reg in qs]  # reg[0] == 1, 2, 3...
    # data = [reg[1] for reg in qs]

    labels = [reg[0] for reg in qs]
    data = [reg[1] for reg in qs]

    return JsonResponse(data={"labels": labels, "num_productos": data})


class PedidosCobrarView(TemplateView):
    template_name = "reportes/pedidos-a-cobrar.html"


def pedidos_a_cobrar(request):
    """ Pedidos no Pagados """

    no_pagados = Pedido.objects.filter(pagado=False).count()
    pagados = Pedido.objects.filter(pagado=True).count()

    data = [pagados, no_pagados]

    return JsonResponse(data={"pedidos": data})


class PedidosPorClienteView(TemplateView):
    template_name = "reportes/pedidos-por-cliente.html"


def pedidos_por_cliente(request):
    """ Pedidos por cliente """

    labels = []
    data = []

    qs = (
        Cliente.objects.values("nombre", "apellido")
        .annotate(num_pedidos=Count("pedidos"))
        .exclude(num_pedidos__lte=0)
    )

    for c in qs:
        full_name = f" {c['nombre']} {c['apellido']}"
        labels.append(full_name)
        data.append(c["num_pedidos"])

    return JsonResponse(data={"labels": labels, "num_pedidos": data})
