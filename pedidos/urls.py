from django.urls import path
from .views import (
    PedidoListView,
    PedidoDetailView,
    PedidoCreateView,
    PedidoUpdateView,
    PedidoDeleteView,
)

app_name = "pedidos"
urlpatterns = [
    path("", PedidoListView.as_view(), name="list"),
    path("new/", PedidoCreateView.as_view(), name="create"),
    path("<int:pk>/", PedidoDetailView.as_view(), name="detail"),
    path("<int:pk>/delete", PedidoDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", PedidoUpdateView.as_view(), name="update"),
]
