from django.urls import path
from .views import Dashboard, LocalidadCreate

app_name = "core"
urlpatterns = [
    path("", Dashboard.as_view(), name="home"),
    # Usada con AJAX en el modalform de creación del cliente
    path("localidad/new/", LocalidadCreate, name="crearLocalidad"),
]
