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
    path("pedidos-tiempo/", PedidosTiempoView.as_view(), name="pedidos-tiempo"),
    path("pedidos-tiempo-json/", pedidos_por_tiempo, name="pedidos-tiempo-json"),
]
