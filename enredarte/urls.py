"""enredarte URL Configuration """

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = []

urlpatterns += [
    path("administracion/", admin.site.urls),
    # Root
    path("", include("core.urls", namespace="core")),
    # Apps
    path("calendario/", include("calendario.urls", namespace="calendario")),
    path("clientes/", include("clientes.urls", namespace="clientes")),
    path("compras/", include("compras.urls", namespace="compras")),
    path("productos/", include("productos.urls", namespace="productos")),
    path("proveedores/", include("proveedores.urls", namespace="proveedores")),
    path("pedidos/", include("pedidos.urls", namespace="pedidos")),
    path("users/", include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)),] + urlpatterns
