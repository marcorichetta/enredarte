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
    path('', ProveedorListView.as_view(), name='index'),
    path('proveedor/new/', ProveedorCreateView.as_view(), name='create'),
    path('proveedor/<int:pk>/', ProveedorDetailView.as_view(), name='detail'),
    path('proveedor/<int:pk>/delete', ProveedorDeleteView.as_view(), name='delete'),
    path('proveedor/<int:pk>/update/', ProveedorUpdateView.as_view(), name='update'),
]