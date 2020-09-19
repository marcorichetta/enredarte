from django.shortcuts import HttpResponseRedirect
from django.db.models import Q
from django.db.models import ProtectedError
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

from core.models import Provincia, Localidad
from .models import Cliente

from django_tables2 import TemplateColumn, SingleTableView, Table, SingleTableMixin
from django_tables2.export.views import ExportMixin
from django_filters import FilterSet, CharFilter
from django_filters.views import FilterView


class ClienteTable(Table):
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
        attrs = {"class": "table table-md"}

    opciones = TemplateColumn(
        template_name="botones_tabla.html",
        extra_context={
            "detail": "clientes:detail",
            "update": "clientes:update",
            "delete": "clientes:delete",
        },
    )


class ClienteFilter(FilterSet):
    class Meta:
        model = Cliente
        fields = {"nombre": ["icontains"], "apellido": ["icontains"]}


class ClienteListView(ExportMixin, SingleTableMixin, FilterView):
    table_class = ClienteTable
    model = Cliente
    template_name = "clientes/clientes.html"
    export_formats = ("csv", "xlsx")

    filterset_class = ClienteFilter

    # def get_queryset(self):
    #     """ Permite buscar en un form dentro de la misma página
    #     con el formato `q?texto` """


class ClienteCreateView(SuccessMessageMixin, CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "telefono", "email", "calle", "numero", "localidad"]
    success_message = "Creado con éxito."

    def get_context_data(self, **kwargs):
        context = super(ClienteCreateView, self).get_context_data(**kwargs)

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
    success_message = "Actualizado con éxito."

    # Modify the template used for this view
    template_name_suffix = "_update_form"


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes:list")
