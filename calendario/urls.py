from django.urls import path
from .views import (
    Calendario,
    get_pedidos,
)

app_name = "calendario"
urlpatterns = [
    # AJAX #
    path("", Calendario.as_view(), name="index"),
    path("get_pedidos/<int:idEstado>", get_pedidos, name="get_pedidos"),
]
