from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    VarianteCreateView,
    VarianteListView
)

urlpatterns = [
    path("", ProductoListView.as_view(), name="producto"),
    path("new/", ProductoCreateView.as_view(), name="createProducto"),
    path("<int:pk>/", ProductoDetailView.as_view(), name="detailProducto"),
    path("<int:pk>/delete", ProductoDeleteView.as_view(), name="deleteProducto"),
    path("<int:pk>/update/", ProductoUpdateView.as_view(), name="updateProducto"),
]

urlpatterns += [
    path("<int:pk>/variantes/", VarianteListView.as_view(), name="variante"),
    path("newvariante/", VarianteCreateView.as_view(), name="createVariante"),
]