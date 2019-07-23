from django.urls import path
from .views import(
    ProveedorListView,
    ProveedorDetailView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView,
)

urlpatterns = [
    path('', ProveedorListView.as_view(), name='proveedor'),
    path('new/',
         ProveedorCreateView.as_view(), name='createProveedor'),
    path('<int:pk>/',
         ProveedorDetailView.as_view(), name='detailProveedor'),
    path('<int:pk>/delete',
         ProveedorDeleteView.as_view(), name='deleteProveedor'),
    path('<int:pk>/update/',
         ProveedorUpdateView.as_view(), name='updateProveedor'),
]
