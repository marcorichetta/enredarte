from django.contrib import admin

from .models import Compra, InsumosCompra


class InsumoInline(admin.TabularInline):
    """Tabular Inline View for Insumo"""

    model = InsumosCompra
    min_num = 1
    max_num = 20
    extra = 1
    exclude = ("is_removed",)


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):

    # https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    # Modificar el qs para que muestre los objetos que fueron eliminados
    def get_queryset(self, request):
        return Compra.all_objects.all()

    """Admin View for Compra"""
    list_display = (
        "id",
        "proveedor",
        "detalles",
        "fecha_compra",
        "created",
        "modified",
        "is_removed",
    )
    list_filter = (
        "created",
        "modified",
        "is_removed",
        "proveedor",
        "fecha_compra",
    )

    autocomplete_fields = ["proveedor"]
    inlines = [InsumoInline]


@admin.register(InsumosCompra)
class InsumosCompraAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "compra",
        "insumo",
        "cantidad",
        "precio_compra",
        "created",
        "modified",
        "is_removed",
    )
    list_filter = ("created", "modified", "is_removed", "compra", "insumo")
    list_display_links = ("compra",)
