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
from productos.views import ProductPriceView, product_dispatch

insumos_urlpatterns = [
    path("", InsumoListView.as_view(), name="list"),
    path("new/", InsumoCreateView.as_view(), name="create"),
    path("<int:pk>/", InsumoDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", InsumoDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", InsumoUpdateView.as_view(), name="update"),
]

regulares_urlpatterns = [
    path("new/", ProductoRegularCreateView.as_view(), name="create"),
    path("<int:pk>/", ProductoRegularDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", ProductoRegularDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", ProductoRegularUpdateView.as_view(), name="update"),
]

irregulares_urlpatterns = [
    path("new/", ProductoIrregularCreateView.as_view(), name="create"),
    path("<int:pk>/", ProductoIrregularDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", ProductoIrregularDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", ProductoIrregularUpdateView.as_view(), name="update"),
]

app_name = "productos"
urlpatterns = [
    path("", ProductoListView.as_view(), name="list"),
    path("precio/", ProductPriceView, name="price"),
    # Redirects
    path("<int:pk>/", product_dispatch, name="detail"),
    path("<int:pk>/delete/", product_dispatch, name="delete"),
    path("<int:pk>/update/", product_dispatch, name="update"),
    # Permite hacer reverse("productos:regular:<name>")
    path("regular/", include((regulares_urlpatterns, "regular"))),
    # /productos/irregular/...
    path("irregular/", include((irregulares_urlpatterns, "irregular"))),
    # /productos/insumos/...
    path("insumos/", include((insumos_urlpatterns, "insumos"))),
]
