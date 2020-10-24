from django.urls import path, include
from .views import ProductoListView

from .views_regular import (
    ProductoRegularCreateView,
    ProductoRegularUpdateView,
    ProductoRegularDetailView,
    ProductoRegularDeleteView,
)

from .views_irregular import (
    ProductoIrregularCreateView,
    ProductoIrregularUpdateView,
    ProductoIrregularDetailView,
    ProductoIrregularDeleteView,
)

from .views_insumos import (
    InsumoListView,
    InsumoCreateView,
    InsumoUpdateView,
    InsumoDetailView,
    InsumoDeleteView,
)
from productos.views import product_dispatch

insumos_urlpatterns = [
    path("", InsumoListView.as_view(), name="insumos-list"),
    path("new/", InsumoCreateView.as_view(), name="insumos-create"),
    path("<int:pk>/", InsumoDetailView.as_view(), name="insumos-detail"),
    path("<int:pk>/delete", InsumoDeleteView.as_view(), name="insumos-delete"),
    path("<int:pk>/update/", InsumoUpdateView.as_view(), name="insumos-update"),
]

regulares_urlpatterns = [
    path("new/", ProductoRegularCreateView.as_view(), name="regular-create"),
    path("<int:pk>/", ProductoRegularDetailView.as_view(), name="regular-detail"),
    path("<int:pk>/delete", ProductoRegularDeleteView.as_view(), name="regular-delete"),
    path("<int:pk>/update/", ProductoRegularUpdateView.as_view(), name="regular-update"),
]

irregulares_urlpatterns = [
    path("new/", ProductoIrregularCreateView.as_view(), name="irregular-create"),
    path("<int:pk>/", ProductoIrregularDetailView.as_view(), name="irregular-detail"),
    path(
        "<int:pk>/delete", ProductoIrregularDeleteView.as_view(), name="irregular-delete"
    ),
    path(
        "<int:pk>/update/", ProductoIrregularUpdateView.as_view(), name="irregular-update"
    ),
]

app_name = "productos"
urlpatterns = [
    path("", ProductoListView.as_view(), name="list"),
    path("new/", ProductoRegularCreateView.as_view(), name="create"),
    # Redirects
    path("<int:pk>/", product_dispatch, name="detail"),
    path("<int:pk>/delete", product_dispatch, name="delete"),
    path("<int:pk>/update/", product_dispatch, name="update"),
    path("regular/", include(regulares_urlpatterns)),
    path("irregular/", include(irregulares_urlpatterns)),
    # Insumos
    path("insumos/", include(insumos_urlpatterns)),
]
