import django_tables2 as tables
from django.views.generic import DetailView
from pedidos.models import OrdenTrabajo
from django_filters import FilterSet
from django_filters.filters import ChoiceFilter, ModelChoiceFilter
from clientes.models import Cliente

from django_tables2.export.views import ExportMixin


class OrdenTrabajoTable(tables.Table):
    class Meta:
        model = OrdenTrabajo
        fields = (
            "id",
            "estado",
            "pedido__cliente",
            "fecha_pedido",
            "fecha_entrega",
            "opciones",
        )
        attrs = {"class": "table table-sm table-hover"}
        order_by = "id"

    opciones = tables.TemplateColumn(
        template_code="""
            <a title="Detalles" class="btn btn-sm btn-outline-primary" href="{% url detail record.pk %}">
                <span data-feather="zoom-in"></span>
            </a>
        """,
        # template_name="botones_tabla.html",
        extra_context={"detail": "pedidos:ot_detail",},
        orderable=False,
    )


class OrdenTrabajoFilter(FilterSet):
    estado = ChoiceFilter(choices=OrdenTrabajo.ESTADO_ORDEN_TRABAJO_CHOICES)

    nombre = ModelChoiceFilter(
        queryset=Cliente.objects.all(), field_name="cliente", label="Cliente"
    )

    class Meta:
        model = OrdenTrabajo
        fields = [
            "estado",
            "pedido__cliente",
        ]


class OrdenTrabajoListView(ExportMixin, tables.SingleTableView):
    table_class = OrdenTrabajoTable
    model = OrdenTrabajo
    filter_class = OrdenTrabajoFilter
    template_name = "pedidos/ordenes.html"
    export_formats = ("csv", "xlsx")
    table_pagination = {"per_page": 10}
    exclude_columns = ("opciones",)  # Excluir columnas del export

    def get_table_data(self):
        """
            Sobreescribe el método utilizado para obtener los registros de la tabla
            De esta manera se devuelve sólo 1 tabla, que puede o no estar filtrada.
            https://stackoverflow.com/a/15129259/6389248
        """

        # Filtra el queryset que se le enviará a la tabla
        self.filter = self.filter_class(
            self.request.GET, queryset=super().get_table_data(),
        )
        return self.filter.qs

    def get_context_data(self, **kwargs):
        """ Inyecta el filtro en el context para usarlo en el template """
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filter
        return context


class OrdenTrabajoDetailView(DetailView):
    model = OrdenTrabajo
    template_name = "pedidos/orden_trabajo_detail.html"

    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     modified_qs = OrdenTrabajo.objects \
    #         .select_related("pedido") \
    #         .prefetch_related("pedido__productos_pedido") \

    #     return modified_qs
