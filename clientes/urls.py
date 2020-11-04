from django.urls import path
from .views import (
    ClienteListView,
    ClienteDetailView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    reporte_clientes,
)

app_name = "clientes"
urlpatterns = [
    path("", ClienteListView.as_view(), name="list"),
    path("new/", ClienteCreateView.as_view(), name="create"),
    path("<int:pk>/", ClienteDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", ClienteDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", ClienteUpdateView.as_view(), name="update"),
    path("reportes/", reporte_clientes, name="reporte"),
]
