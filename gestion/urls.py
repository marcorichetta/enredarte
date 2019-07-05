from django.urls import path
from .views import (
    ProveedorListView,
    ProveedorDetailView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView
)
from . import views

urlpatterns = [
    path('', ProveedorListView.as_view(), name='proveedor'),
    path('proveedores/new/',
         ProveedorCreateView.as_view(), name='createProveedor'),
    path('proveedores/<int:pk>/',
         ProveedorDetailView.as_view(), name='detailProveedor'),
    path('proveedores/<int:pk>/delete',
         ProveedorDeleteView.as_view(), name='deleteProveedor'),
    path('proveedores/<int:pk>/update/',
         ProveedorUpdateView.as_view(), name='updateProveedor'),
]
