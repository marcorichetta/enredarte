"""enredarte URL Configuration """

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = []

urlpatterns += [
    path("admin/", admin.site.urls, name="admin"),
    # Root
    path("", include("core.urls")),
    # Apps
    path("calendario/", include("calendario.urls")),
    path("clientes/", include("clientes.urls")),
    path("compras/", include("compras.urls")),
    path("productos/", include("productos.urls")),
    path("proveedores/", include("proveedores.urls")),
    path("pedidos/", include("pedidos.urls")),
    path("users/", include("users.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)),] + urlpatterns
