import django_tables2 as tables
from core.mixins import DeleteSuccessMessageMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.template.defaultfilters import floatformat
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters import FilterSet
from django_filters.filters import ModelChoiceFilter
from django_tables2.export.views import ExportMixin
from proveedores.models import Proveedor

from .forms import CompraForm, InsumosCompraFormset
from .models import Compra


class CompraTable(tables.Table):
    class Meta:
        model = Compra
        fields = ("id", "proveedor", "precio_total", "fecha_compra", "opciones")
        attrs = {"class": "table table-sm table-hover"}
        order_by = "id"

    def render_precio_total(self, value):
        """ Función para modificar como se muestra el precio de venta en el template """
        precio = floatformat(value)
        return f"$ {precio}"

    opciones = tables.TemplateColumn(
        template_name="botones_tabla.html",
        extra_context={
            "detail": "compras:detail",
            "update": "compras:update",
            "delete": "compras:delete",
        },
    )


class CompraFilter(FilterSet):
    nombre = ModelChoiceFilter(
        queryset=Proveedor.objects.all(),
        field_name="proveedor",
        label="Buscar por proveedor",
    )

    class Meta:
        model = Compra
        fields = [
            "proveedor",
        ]


class CompraListView(ExportMixin, tables.SingleTableView):
    model = Compra
    table_class = CompraTable
    filter_class = CompraFilter
    template_name = "compras/compras.html"
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


class CompraCreateView(SuccessMessageMixin, CreateView):
    model = Compra
    form_class = CompraForm
    success_message = "La compra fue creada con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Le agregamos los insumos al context para usarlos en el template
        if self.request.POST:
            context["insumos"] = InsumosCompraFormset(self.request.POST)
        else:
            context["insumos"] = InsumosCompraFormset()
        return context

    def form_valid(self, form):
        # Obtener info de compra e insumos posteados en el form
        context = self.get_context_data()
        formset_insumos = context["insumos"]

        # Guardar la compra
        self.object = form.save()
        # Si son válidos los insumos se guardan
        if formset_insumos.is_valid():
            formset_insumos.instance = self.object
            formset_insumos.save()

            # Guardar compra completa
            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))


class CompraUpdateView(SuccessMessageMixin, UpdateView):
    model = Compra
    form_class = CompraForm
    success_message = "La compra fue actualizada con éxito."
    # Modify the template used for this view
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Enviar el objeto como instancia para ser actualizado
        if self.request.POST:
            context["insumos"] = InsumosCompraFormset(
                self.request.POST, instance=self.object
            )
        else:
            context["insumos"] = InsumosCompraFormset(instance=self.object)
        return context

    def form_valid(self, form):
        # Obtenemos info de la compra e insumos posteados en el form
        context = self.get_context_data()
        insumos = context["insumos"]

        self.object = form.save()

        if insumos.is_valid():
            insumos.instance = self.object
            insumos.save()
            # Guardar compra completo
            return super(CompraUpdateView, self).form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("compras:detail", kwargs={"pk": self.object.pk})


class CompraDetailView(DetailView):
    model = Compra

    def get_context_data(self, *args, **kwargs):
        context = super(CompraDetailView, self).get_context_data(*args, **kwargs)
        return context


class CompraDeleteView(DeleteSuccessMessageMixin, DeleteView):
    model = Compra
    success_url = reverse_lazy("compras:list")
    success_message = "La compra fue eliminada con éxito."
