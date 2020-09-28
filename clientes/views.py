from django.contrib.messages.views import SuccessMessageMixin
from core.mixins import DeleteSuccessMessageMixin
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from core.models import Provincia, Localidad
from .models import Cliente

import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from django_filters import FilterSet, CharFilter
from django_filters.views import FilterView


class ClienteTable(tables.Table):
    class Meta:
        model = Cliente
        fields = (
            "id",
            "nombre",
            "apellido",
            "email",
            "telefono",
            "localidad",
            "opciones",
        )
        attrs = {"class": "table table-sm table-hover"}

    opciones = tables.TemplateColumn(
        template_name="botones_tabla.html",
        extra_context={
            "detail": "clientes:detail",
            "update": "clientes:update",
            "delete": "clientes:delete",
        },
    )


class ClienteFilter(FilterSet):
    nombre = CharFilter(
        field_name="nombre", lookup_expr="icontains", label="Buscar por nombre"
    )
    apellido = CharFilter(
        field_name="apellido", lookup_expr="icontains", label="Buscar por apellido"
    )

    class Meta:
        model = Cliente
        fields = [
            "nombre",
            "apellido",
        ]


class ClienteListView(ExportMixin, tables.SingleTableView):
    table_class = ClienteTable
    model = Cliente
    filter_class = ClienteFilter
    template_name = "clientes/clientes.html"
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
        """ Incluye el filtro en el context para poder instanciarlo en el template """

        context = super().get_context_data(**kwargs)
        context["filter"] = self.filter
        return context


class ClienteCreateView(SuccessMessageMixin, CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "telefono", "email", "calle", "numero", "localidad"]
    success_message = "El cliente fue creado con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Devuelve una lista con los id y los nombres de localidades y provincias
        # Se usan en el form original y en el modal para crear nueva localidad
        context["localidades"] = Localidad.objects.get_queryset()
        context["provincias"] = Provincia.objects.get_queryset()

        return context


class ClienteDetailView(DetailView):
    model = Cliente


class ClienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Cliente
    fields = [
        "nombre",
        "apellido",
        "telefono",
        "email",
        "calle",
        "numero",
        "localidad",
        "detalles",
    ]
    success_message = "El cliente fue actualizado con éxito."

    # Modify the template used for this view
    template_name_suffix = "_update_form"


class ClienteDeleteView(DeleteSuccessMessageMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes:list")
    success_message = "El cliente fue eliminado con éxito."
