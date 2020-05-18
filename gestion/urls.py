from django.urls import path
from .views import Dashboard, LocalidadCreate


urlpatterns = [
    path("", Dashboard.as_view(), name="index"),
    # Usada con AJAX en el modalform de creación del cliente
    path("localidad/new/", LocalidadCreate, name="crearLocalidad"),
]
