import django_tables2 as tables
from clientes.models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    TemplateView,
    UpdateView,
)
from django_filters import CharFilter, FilterSet
from django_tables2.export.views import ExportMixin
from pedidos.models import Pedido

from core.mixins import DeleteSuccessMessageMixin

from .models import Localidad, Provincia

# Create your views here.


class Dashboard(LoginRequiredMixin, TemplateView):
    """ Panel principal que contiene información útil para el usuario """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)

        context["url_pedidos_en_proceso"] = "%s?estado=1" % reverse_lazy("pedidos:list")
        context["url_pedidos_listos"] = "%s?estado=2" % reverse_lazy("pedidos:list")

        context["pedidos_en_proceso"] = Pedido.objects.filter(estado=Pedido.EN_PROCESO)
        context["pedidos_listos"] = Pedido.objects.filter(estado=Pedido.LISTO)

        return context


@require_http_methods(["POST"])
def LocalidadCreate(request):
    cod_postal = request.POST.get("cod_postal")
    localidad = request.POST.get("localidad")
    provincia_id = request.POST.get("provincia_id")

    if len(cod_postal) != 4:

        mensaje = "ERROR: El código postal ingresado tiene más de 4 dígitos."

        data = {
            "status": "false",
            "mensaje": mensaje,
        }

        return JsonResponse(data, status=400,)

        # return HttpResponse(json.dumps(context), content_type="application/json", status_code=500)

    # Obtener instancia de Provincia
    provincia = Provincia.objects.get(pk=provincia_id)

    # Crear en DB
    nueva_localidad = Localidad.objects.create(
        cod_postal=cod_postal, localidad=localidad, provincia=provincia
    )

    # Enviar dict con datos de la nueva Localidad
    data = {
        "pk_value": nueva_localidad.pk,
        "localidad": nueva_localidad.localidad,
        "provincia": provincia_id,
    }

    # Devolver info a JS
    return JsonResponse(data)


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
        template_code="""
            <a title="Detalles" class="btn btn-sm btn-outline-primary" href="{% url detail record.pk %}">
                <span data-feather="zoom-in"></span>
            </a>
            <a title="Editar" class="btn btn-sm btn-outline-secondary" href="{% url update record.pk %}">
                <span data-feather="edit-3"></span>
            </a>
        """,
        # template_name="botones_tabla.html",
        extra_context={
            "detail": "core:localidades-detail",
            "update": "core:localidades-update",
            # "delete": "core:localidades-delete",
        },
        orderable=False,
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

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.select_related("provincia")

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
