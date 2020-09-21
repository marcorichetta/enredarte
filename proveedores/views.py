from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from core.models import Localidad, Provincia
from .models import Proveedor

import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from django_filters import FilterSet, CharFilter, NumberFilter
from django_filters.views import FilterView


class ProveedorTable(tables.Table):
    class Meta:
        model = Proveedor
        fields = (
            "id",
            "razon_social",
            "cuit",
            "telefono",
            "email",
            "localidad",
            "opciones",
        )
        attrs = {"class": "table table-sm table-hover"}

    opciones = tables.TemplateColumn(
        template_name="botones_tabla.html",
        extra_context={
            "detail": "proveedores:detail",
            "update": "proveedores:update",
            "delete": "proveedores:delete",
        },
    )


class ProveedorFilter(FilterSet):
    razon_social = CharFilter(
        field_name="razon_social", lookup_expr="icontains", label="Buscar por nombre"
    )
    cuit = CharFilter(field_name="cuit", lookup_expr="icontains", label="Buscar por CUIT")

    class Meta:
        model = Proveedor
        fields = ["razon_social", "cuit", "localidad"]


class ProveedorListView(ExportMixin, tables.SingleTableView):
    table_class = ProveedorTable
    model = Proveedor
    filter_class = ProveedorFilter
    template_name = "proveedores/proveedores.html"
    export_formats = ("csv", "xlsx")
    table_pagination = {"per_page": 20}
    exclude_columns = ("opciones",)

    def get_table_data(self):
        """
            Sobreescribe el método utilizado para obtener los registros de la tabla
            De esta manera se devuelve sólo 1 tabla, que puede o no estar filtrada.
            https://stackoverflow.com/a/15129259/6389248
        """
        self.filter = self.filter_class(
            self.request.GET, queryset=super().get_table_data()
        )
        return self.filter.qs

    def get_context_data(self, **kwargs):
        """ Devuelve el texto buscado para usarlo en la paginación """
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filter
        return context


class ProveedorCreateView(SuccessMessageMixin, CreateView):
    model = Proveedor
    fields = ["cuit", "razon_social", "telefono", "email", "calle", "numero", "localidad"]
    success_message = "Creado con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Devuelve una lista con los id y los nombres de localidades y provincias
        # Se usan en el form original y en el modal para crear nueva localidad
        context["localidades"] = Localidad.objects.get_queryset()
        context["provincias"] = Provincia.objects.get_queryset()

        return context


class ProveedorDetailView(DetailView):
    model = Proveedor


class ProveedorUpdateView(SuccessMessageMixin, UpdateView):
    model = Proveedor
    fields = [
        "cuit",
        "razon_social",
        "telefono",
        "email",
        "calle",
        "numero",
        "localidad",
        "detalles",
    ]
    success_message = "Actualizado con éxito."

    # Modify the template used for this view
    template_name_suffix = "_update_form"


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    success_url = reverse_lazy("proveedores:list")
