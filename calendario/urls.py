from django.urls import path
from .views import (
    Calendario,
    get_pedidos,
)

urlpatterns = [
    # AJAX #
    path("", Calendario.as_view(), name='calendario.index'),
    path("get_pedidos/<int:idEstado>", get_pedidos, name='get_pedidos'),
]