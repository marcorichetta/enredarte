from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    VarianteListView,
)

urlpatterns = [
    path("", ProductoListView.as_view(), name="producto"),
    path("new/", ProductoCreateView.as_view(), name="createProducto"),
    path("<int:pk>/", ProductoDetailView.as_view(), name="detailProducto"),
    path("<int:pk>/delete", ProductoDeleteView.as_view(), name="deleteProducto"),
    path("<int:pk>/update/", ProductoUpdateView.as_view(), name="updateProducto"),

    path("variantes/", VarianteListView.as_view(), name="createVariante"),
]
