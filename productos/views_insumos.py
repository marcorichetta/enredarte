import django_tables2 as tables
from core.mixins import DeleteSuccessMessageMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django_filters import CharFilter, FilterSet
from django_tables2.export.views import ExportMixin

from .forms_insumos import InsumoForm
from .models import Insumo
from django.template.defaultfilters import floatformat


class InsumoTable(tables.Table):
    class Meta:
        model = Insumo
        fields = (
            "id",
            "nombre",
            "medida",
            "precio",
            "proveedores",
            "opciones",
        )
        attrs = {"class": "table table-sm table-hover"}
        order_by = "id"

    def render_medida(self, value, record):
        """
            Modifica como se muestra la columna medida
            (Valor más la unidad de medida en la misma celda)
        """
        return f"{value} {record.unidad_medida}"

    def render_precio(self, value):
        """ Función para modificar como se muestra el precio de venta en el template """
        precio = floatformat(value)
        return f"$ {precio}"

    opciones = tables.TemplateColumn(
        template_name="botones_tabla.html",
        extra_context={
            "detail": "productos:insumos:detail",
            "update": "productos:insumos:update",
            "delete": "productos:insumos:delete",
        },
        orderable=False,
    )


class InsumoFilter(FilterSet):
    nombre = CharFilter(
        field_name="nombre", lookup_expr="icontains", label="Buscar por nombre"
    )

    class Meta:
        model = Insumo
        fields = ["nombre"]


class InsumoListView(ExportMixin, tables.SingleTableView):
    table_class = InsumoTable
    model = Insumo
    filter_class = InsumoFilter
    template_name = "insumos/insumos.html"
    export_formats = ("csv", "xlsx")
    table_pagination = {"per_page": 10}
    exclude_columns = ("opciones",)  # Excluir columnas del export

    def get_table_data(self):
        """
            Sobreescribe el método utilizado para obtener los registros de la tabla
            De esta manera se devuelve sólo 1 tabla, que puede o no estar filtrada.
            https://stackoverflow.com/a/15129259/6389248
        """

        self.filter = self.filter_class(
            self.request.GET, queryset=super().get_table_data(),
        )
        return self.filter.qs

    def get_context_data(self, **kwargs):
        """ Inyecta el filtro en el context para usarlo en el template """
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filter
        return context


class InsumoCreateView(SuccessMessageMixin, CreateView):
    model = Insumo
    form_class = InsumoForm
    template_name = "insumos/insumo_form.html"
    success_message = "El insumo fue creado con éxito."

    def get_success_url(self):
        return reverse_lazy("productos:insumos:detail", kwargs={"pk": self.object.pk})


class InsumoUpdateView(SuccessMessageMixin, UpdateView):
    model = Insumo
    form_class = InsumoForm
    template_name = "insumos/insumo_update_form.html"

    template_name_suffix = "_update_form"
    success_message = "El insumo fue actualizado con éxito."

    def get_success_url(self):
        return reverse_lazy("productos:insumos:detail", kwargs={"pk": self.object.pk})


class InsumoDetailView(DetailView):
    model = Insumo
    template_name = "insumos/insumo_detail.html"


class InsumoDeleteView(DeleteSuccessMessageMixin, DeleteView):
    model = Insumo
    template_name = "insumos/insumo_confirm_delete.html"

    success_url = reverse_lazy("productos:insumos:list")
    success_message = "El insumo fue eliminado con éxito."
