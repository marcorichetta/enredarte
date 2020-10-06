from django.contrib import admin

from .models import Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):

    # https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    # Modificar el qs para que muestre los objetos que fueron eliminados
    def get_queryset(self, request):
        return Proveedor.all_objects.all()

    list_display = (
        "cuit",
        "razon_social",
        "telefono",
        "email",
        "calle",
        "numero",
        "localidad",
        "created",
        "modified",
        "is_removed",
    )
    list_filter = ("created", "modified", "is_removed", "localidad")
    search_fields = ("cuit", "razon_social")
    list_display_links = ("razon_social",)
    ordering = ("razon_social",)
