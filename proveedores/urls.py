from django.urls import path
from .views import (
    ProveedorListView,
    ProveedorDetailView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView,
)

app_name = "proveedores"
urlpatterns = [
    path("", ProveedorListView.as_view(), name="list"),
    path("new/", ProveedorCreateView.as_view(), name="create"),
    path("<int:pk>/", ProveedorDetailView.as_view(), name="detail"),
    path("<int:pk>/delete", ProveedorDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", ProveedorUpdateView.as_view(), name="update"),
]
