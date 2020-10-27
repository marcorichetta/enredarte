import django_tables2 as tables
from django.template.defaultfilters import floatformat
from django_filters.filters import CharFilter, ChoiceFilter
from django_filters import FilterSet
from django_tables2.export.views import ExportMixin

from .models import Producto
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect


class ProductoTable(tables.Table):

    get_precio = tables.Column(verbose_name="Precio", orderable=False)

    class Meta:
        model = Producto
        fields = (
            "id",
            "tipo",
            "nombre",
            "descripcion",
            "get_precio",
            "opciones",
        )
        attrs = {"class": "table table-sm table-hover"}
        order_by = "id"

    def render_get_precio(self, value):
        """ Función para modificar como se muestra el precio de venta en el template """
        precio = floatformat(value)
        return f"$ {precio}"

    opciones = tables.TemplateColumn(
        template_name="botones_tabla.html",
        extra_context={
            "detail": "productos:detail",
            "update": "productos:update",
            "delete": "productos:delete",
        },
        orderable=False,
    )


class ProductoFilter(FilterSet):
    nombre = CharFilter(
        field_name="nombre", lookup_expr="icontains", label="Buscar por nombre"
    )

    tipo = ChoiceFilter(
        field_name="tipo", label="Filtrar por tipo", choices=Producto.TIPOS
    )

    class Meta:
        model = Producto
        fields = ["nombre", "tipo"]


class ProductoListView(ExportMixin, tables.SingleTableView):
    table_class = ProductoTable
    model = Producto
    filter_class = ProductoFilter
    template_name = "productos/productos.html"
    export_formats = ("csv", "xlsx")
    table_pagination = {"per_page": 10}
    exclude_columns = ("opciones",)  # Excluir columnas del export

    def get_queryset(self):
        qs = super().get_queryset()

        modified_qs = (
            qs.select_related("regular")
            .select_related("irregular")
            .prefetch_related("insumos")
        )

        return modified_qs

    def get_table_data(self):
        """
            Sobreescribe el método utilizado para obtener los registros de la tabla
            De esta manera se devuelve sólo 1 tabla, que puede o no estar filtrada.
            https://stackoverflow.com/a/15129259/6389248
        """

        # v: Variable = Variable.objects.get(pk=1)
        # qs = Producto.objects \
        #     .select_related("insumo_base") \
        #     .select_related("insumo_lados") \
        #     .annotate(
        #         precioBase=(F('largo') / 100) * (F('ancho') / 100) * F('insumo_base__precio'),
        #         precioLatCorto=(F('ancho') / 100) * (F('alto') / 100),
        #         precioLatLargo=(F('largo') / 100) * (F('alto') / 100),
        #         horas=F('tiempo') / 60,
        #         precio_tiempo=F('horas') * v.precio_hora,
        #         precio_costo=ExpressionWrapper(F('precioBase') + F('precioLatCorto') + F('precioLatLargo') + F('precio_tiempo'), output_field=DecimalField()),
        #         precio_venta_crudo=F('precio_costo') * ((v.ganancia_por_menor / 100) + 1),
        #         tiempo_terminado=F('tiempo') * 2 / 60,
        #         precio_tiempo_terminado=F('tiempo_terminado') * v.precio_hora,
        #         precio_terminado=ExpressionWrapper(F('precio_costo') + v.precio_pintado + F('precio_tiempo_terminado'), output_field=DecimalField()),
        #         precio_venta_terminado=F('precio_terminado') * ((v.ganancia_por_menor / 100) + 1)
        #     )

        self.filter = self.filter_class(
            self.request.GET, queryset=super().get_table_data(),
        )
        return self.filter.qs

    def get_context_data(self, **kwargs):
        """ Inyecta el filtro en el context para usarlo en el template """
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filter
        return context


def product_dispatch(request, pk: int):
    """
        View para redireccionar los productos regulares e irregulares.
        Recibe la request con el pk del producto y redirige según el tipo de producto.
    """
    prod: Producto = get_object_or_404(Producto, pk=pk)

    if prod.tipo == Producto.TIPOS.regular:

        if "update" in request.path:
            return redirect("productos:regular:update", pk=pk)

        if "delete" in request.path:
            return redirect("productos:regular:delete", pk=pk)

        return redirect("productos:regular:detail", pk=pk)

    else:
        if "update" in request.path:
            return redirect("productos:irregular:update", pk=pk)

        if "delete" in request.path:
            return redirect("productos:irregular:delete", pk=pk)

        return redirect("productos:irregular:detail", pk=pk)

    raise Http404()
