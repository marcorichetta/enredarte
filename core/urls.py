from django.urls import path
from .views import (
    Dashboard,
    LocalidadCreate,
    LocalidadListView,
    LocalidadCreateView,
    LocalidadUpdateView,
    LocalidadDetailView,
    LocalidadDeleteView,
)

app_name = "core"
urlpatterns = [
    path("", Dashboard.as_view(), name="home"),
    # Usada con AJAX en el modalform de creación del cliente
    path("localidad/", LocalidadListView.as_view(), name="localidades-list"),
    path("localidad/new/", LocalidadCreateView.as_view(), name="localidades-create"),
    path("localidad/<int:pk>/", LocalidadDetailView.as_view(), name="localidades-detail"),
    path(
        "localidad/<int:pk>/update/",
        LocalidadUpdateView.as_view(),
        name="localidades-update",
    ),
    path(
        "localidad/<int:pk>/delete/",
        LocalidadDeleteView.as_view(),
        name="localidades-delete",
    ),
    # AJAX
    path("localidad/ajax-new/", LocalidadCreate, name="crearLocalidad"),
]
