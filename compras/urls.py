from django.urls import path

from .views import (
    CompraListView,
    CompraCreateView,
    CompraDetailView,
    CompraUpdateView,
    CompraDeleteView,
)

urlpatterns = [
    path("", CompraListView.as_view(), name="compra"),
    path("new/", CompraCreateView.as_view(), name="createCompra"),
    path("<int:pk>/", CompraDetailView.as_view(), name="detailCompra"),
    path("<int:pk>/update/", CompraUpdateView.as_view(), name="updateCompra"),
    path("<int:pk>/delete/", CompraDeleteView.as_view(), name="deleteCompra"),
]
