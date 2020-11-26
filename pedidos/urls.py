from django.urls import path
from .views import (
    PedidoListView,
    PedidoDetailView,
    PedidoCreateView,
    PedidoUpdateView,
    PedidoDeleteView,
)

from pedidos.views_orden_trabajo import OrdenTrabajoDetailView
from pedidos.views_core import PedidoEnProcesoView, OrdenTrabajoFinalizadaView

app_name = "pedidos"
urlpatterns = [
    path("", PedidoListView.as_view(), name="list"),
    path("new/", PedidoCreateView.as_view(), name="create"),
    path("<int:pk>/", PedidoDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", PedidoDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", PedidoUpdateView.as_view(), name="update"),
    path("orden_trabajo/<int:pk>/", OrdenTrabajoDetailView.as_view(), name="ot_detail"),
    # Estado Pedido
    path("pagar/", PedidoEnProcesoView, name="pagar"),
    path("finalizar_ot/", OrdenTrabajoFinalizadaView, name="finalizar_ot"),
]
