from django.urls import path, include
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoRegularCreateView,
    ProductoRegularUpdateView,
    ProductoDeleteView,
)

from .views_insumos import (
    InsumoListView,
    InsumoCreateView,
    InsumoUpdateView,
    InsumoDetailView,
    InsumoDeleteView,
)

insumos_urlpatterns = [
    path("", InsumoListView.as_view(), name="insumos-list"),
    path("new/", InsumoCreateView.as_view(), name="insumos-create"),
    path("<int:pk>/", InsumoDetailView.as_view(), name="insumos-detail"),
    path("<int:pk>/delete", InsumoDeleteView.as_view(), name="insumos-delete"),
    path("<int:pk>/update/", InsumoUpdateView.as_view(), name="insumos-update"),
]

app_name = "productos"
urlpatterns = [
    path("", ProductoListView.as_view(), name="list"),
    path("new/", ProductoRegularCreateView.as_view(), name="create"),
    path("<int:pk>/", ProductoDetailView.as_view(), name="detail"),
    path("<int:pk>/delete", ProductoDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", ProductoRegularUpdateView.as_view(), name="update"),
    # Insumos
    path("insumos/", include(insumos_urlpatterns)),
]
