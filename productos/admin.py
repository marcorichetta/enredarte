from django.contrib import admin

from .models import Insumo, Unidad, Producto, StockInsumo, InsumosProducto, ProductImage

# Register your models here.


@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Unidad.all_objects.all()

    list_display = ("id", "created", "modified", "is_removed", "nombre", "descripcion")

    list_filter = ("created", "modified", "is_removed")


@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Insumo.all_objects.all()

    list_display = (
        "id",
        "nombre",
        "descripcion",
        "medida",
        "unidad_medida",
        "precio",
        "created",
        "modified",
        "is_removed",
    )
    list_filter = ("unidad_medida",)

    # Autocompletion on CompraAdmin
    autocomplete_fields = ("proveedores",)


@admin.register(StockInsumo)
class StockInsumoAdmin(admin.ModelAdmin):
    list_display = ("id", "insumo", "cantidad", "detalles")
    list_filter = ("insumo",)


class InsumoInline(admin.TabularInline):
    """Tabular Inline View for Insumo"""

    model = InsumosProducto
    min_num = 0
    max_num = 5
    extra = 1
    exclude = ("is_removed",)


class ProductImageInline(admin.TabularInline):
    """Tabular Inline View for ProductImag"""

    model = ProductImage
    min_num = 0
    max_num = 3
    extra = 1
    exclude = ("is_removed",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Producto.all_objects.all()

    list_display = (
        "id",
        "nombre",
        "descripcion",
        "largo",
        "ancho",
        "alto",
        "tiempo",
        "insumo_base",
        "insumo_lados",
        "created",
        "modified",
        "is_removed",
    )

    list_filter = ("insumo_base", "insumo_lados", "created", "modified", "is_removed")
    search_fields = ["id, nombre"]
    inlines = [ProductImageInline, InsumoInline]


@admin.register(InsumosProducto)
class InsumosProductoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return InsumosProducto.all_objects.all()

    list_display = (
        "id",
        "producto",
        "insumo",
        "cantidad",
        "created",
        "modified",
        "is_removed",
    )
    list_filter = ("producto", "insumo")
