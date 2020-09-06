from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
)

app_name = "productos"
urlpatterns = [
    path("", ProductoListView.as_view(), name="list"),
    path("new/", ProductoCreateView.as_view(), name="create"),
    path("<int:pk>/", ProductoDetailView.as_view(), name="detail"),
    path("<int:pk>/delete", ProductoDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", ProductoUpdateView.as_view(), name="update"),
]
