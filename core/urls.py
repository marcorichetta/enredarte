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
    path("localidades/", LocalidadListView.as_view(), name="localidades-list"),
    path("localidades/new/", LocalidadCreateView.as_view(), name="localidades-create"),
    path(
        "localidades/<int:pk>/", LocalidadDetailView.as_view(), name="localidades-detail"
    ),
    path(
        "localidades/<int:pk>/update/",
        LocalidadUpdateView.as_view(),
        name="localidades-update",
    ),
    path(
        "localidades/<int:pk>/delete/",
        LocalidadDeleteView.as_view(),
        name="localidades-delete",
    ),
    # AJAX
    path("localidades/ajax-new/", LocalidadCreate, name="crearLocalidad"),
]
