from django.urls import path
from reportes.views import *

app_name = "reportes"

urlpatterns = [
    path("", ReportesView.as_view(), name="list"),
    path(
        "clientes-localidad/", ClientesLocalidadView.as_view(), name="clientes-localidad"
    ),
    path(
        "clientes-localidad-json/", cliente_por_localidad, name="clientes-localidad-json"
    ),
    #####
    path(
        "productos-solicitados/",
        ProductosMasSolicitadosView.as_view(),
        name="productos-solicitados",
    ),
    path(
        "productos-solicitados-json/",
        productos_mas_solicitados,
        name="productos-solicitados-json",
    ),
    #####
    path("pedidos-tiempo/", PedidosTiempoView.as_view(), name="pedidos-tiempo"),
    path("pedidos-tiempo-json/", pedidos_por_tiempo, name="pedidos-tiempo-json"),
    #####
    path("pedidos-a-cobrar/", PedidosCobrarView.as_view(), name="pedidos-a-cobrar"),
    path("pedidos-a-cobrar-json/", pedidos_a_cobrar, name="pedidos-a-cobrar-json"),
    #####
    path(
        "pedidos-por-cliente/",
        PedidosPorClienteView.as_view(),
        name="pedidos-por-cliente",
    ),
    path(
        "pedidos-por-cliente-json/", pedidos_por_cliente, name="pedidos-por-cliente-json"
    ),
]
