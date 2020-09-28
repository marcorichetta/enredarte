from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from pedidos.models import Pedido
from clientes.models import Cliente
from productos.models import Producto

from .models import Localidad, Provincia


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

import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from django_filters import FilterSet, CharFilter
from django_filters.views import FilterView
from django_filters.filters import NumberFilter

# Create your views here.


class Dashboard(LoginRequiredMixin, TemplateView):
    """ Panel principal que contiene información útil para el usuario """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context["pedidos"] = Pedido.objects.get_queryset()[:5]
        context["clientes"] = Cliente.objects.get_queryset()
        context["productos"] = Producto.objects.get_queryset()[:5]

        return context


@require_http_methods(["POST"])
def LocalidadCreate(request):
    cod_postal = request.POST.get("cod_postal")
    localidad = request.POST.get("localidad")
    provincia_id = request.POST.get("provincia_id")

    # Obtener instancia de Provincia
    provincia = Provincia.objects.get(pk=provincia_id)

    # Crear en DB
    Localidad.objects.create(
        cod_postal=cod_postal, localidad=localidad, provincia=provincia
    )

    # Enviar dict con datos de la nueva Localidad
    nuevaLocalidad = {
        "cod_postal": cod_postal,
        "localidad": localidad,
        "provincia": provincia_id,
    }

    # Devolver info a JS
    return JsonResponse(nuevaLocalidad)


class LocalidadTable(tables.Table):
    class Meta:
        model = Localidad
        fields = (
            "id",
            "cod_postal",
            "localidad",
            "provincia",
            "opciones",
        )
        attrs = {"class": "table table-sm table-hover"}
        order_by = "id"

    opciones = tables.TemplateColumn(
        template_name="botones_tabla.html",
        extra_context={
            "detail": "core:localidades-detail",
            "update": "core:localidades-update",
            "delete": "core:localidades-delete",
        },
    )


class LocalidadFilter(FilterSet):

    localidad = CharFilter(
        field_name="localidad", lookup_expr="icontains", label="Buscar por localidad"
    )

    cod_postal = CharFilter(
        field_name="cod_postal",
        lookup_expr="icontains",
        label="Buscar por Código Postal",
    )

    class Meta:
        model = Localidad
        fields = [
            "cod_postal",
            "localidad",
            "provincia",
        ]


class LocalidadListView(ExportMixin, tables.SingleTableView):
    table_class = LocalidadTable
    model = Localidad
    filter_class = LocalidadFilter
    template_name = "core/localidades.html"
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


class LocalidadCreateView(SuccessMessageMixin, CreateView):
    model = Localidad
    fields = [
        "cod_postal",
        "localidad",
        "provincia",
    ]
    success_message = "La localidad fue creada con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["provincias"] = Provincia.objects.get_queryset()

        return context

    def get_success_url(self):
        return reverse_lazy("core:localidades-detail", kwargs={"pk": self.object.pk})


class LocalidadUpdateView(SuccessMessageMixin, UpdateView):
    model = Localidad
    fields = [
        "provincia",
        "localidad",
        "cod_postal",
    ]
    # template_name="core/localidad_update_form.html"
    template_name_suffix = "_update_form"
    success_message = "La localidad fue actualizada con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["provincias"] = Provincia.objects.get_queryset()

        return context

    def get_success_url(self):
        return reverse_lazy("core:localidades-detail", kwargs={"pk": self.object.pk})


class LocalidadDetailView(DetailView):
    model = Localidad

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class LocalidadDeleteView(DeleteSuccessMessageMixin, DeleteView):
    model = Localidad
    success_url = reverse_lazy("core:localidades-list")
    success_message = "La localidad fue eliminada con éxito."
