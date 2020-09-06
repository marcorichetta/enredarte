from django.urls import path

from .views import (
    CompraListView,
    CompraCreateView,
    CompraDetailView,
    CompraUpdateView,
    CompraDeleteView,
)

app_name = "compras"
urlpatterns = [
    path("", CompraListView.as_view(), name="list"),
    path("new/", CompraCreateView.as_view(), name="create"),
    path("<int:pk>/", CompraDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CompraUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CompraDeleteView.as_view(), name="delete"),
]
