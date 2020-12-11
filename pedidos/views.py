import django_tables2 as tables
from calendario.widgets import MultiDatePicker
from clientes.models import Cliente
from core.mixins import DeleteSuccessMessageMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.template.defaultfilters import floatformat
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters import FilterSet
from django_filters.filters import (
    BooleanFilter,
    ChoiceFilter,
    DateFromToRangeFilter,
    ModelChoiceFilter,
)
from django_tables2.export.views import ExportMixin

from .forms import PedidoForm, ProductosPedidoFormset
from .models import Pedido
from pedidos.forms import DescuentoSoloLecturaForm


class PedidoTable(tables.Table):
    class Meta:
        model = Pedido
        fields = (
            "id",
            "estado",
            "cliente",
            "get_precio_total",
            "fecha_pedido",
            "fecha_entrega",
            "opciones",
        )
        attrs = {"class": "table table-sm table-hover"}
        order_by = "id"

    def render_get_precio_total(self, value):
        """ Función para modificar como se muestra el precio de venta en el template """
        # precio_total, _ = value
        precio_total = floatformat(value)
        return f"$ {precio_total}"

    get_precio_total = tables.Column(verbose_name="Precio total", orderable=False)

    opciones = tables.TemplateColumn(
        template_name="botones_tabla.html",
        extra_context={
            "detail": "pedidos:detail",
            "update": "pedidos:update",
            "delete": "pedidos:delete",
        },
        orderable=False,
    )


class PedidoFilter(FilterSet):
    estado = ChoiceFilter(choices=Pedido.ESTADO_PEDIDO_CHOICES)

    nombre = ModelChoiceFilter(
        queryset=Cliente.objects.all(), field_name="cliente", label="Cliente"
    )

    fecha_entrega = DateFromToRangeFilter(
        field_name="fecha_entrega",
        widget=MultiDatePicker(attrs={"placeholder": "DD/MM/YYYY"}),
        label="Rango de fechas de entrega",
    )

    pagado = BooleanFilter(field_name="pagado", label="Pagado")

    class Meta:
        model = Pedido
        fields = ["estado", "cliente", "fecha_entrega", "pagado"]


class PedidoListView(ExportMixin, tables.SingleTableView):
    table_class = PedidoTable
    model = Pedido
    filter_class = PedidoFilter
    template_name = "pedidos/pedidos.html"
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


class PedidoCreateView(SuccessMessageMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    success_message = "El pedido fue creado con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Le agregamos los productos al context para usarlos en el template
        if self.request.POST:
            context["productos"] = ProductosPedidoFormset(self.request.POST)
        else:
            context["productos"] = ProductosPedidoFormset()

        # Campo descuento como readonly si el usuario no tiene el permiso
        if not self.request.user.has_perm("pedidos.change_discount"):
            context["form"] = DescuentoSoloLecturaForm()

        return context

    def form_valid(self, form):
        # Obtener info de pedido y productos posteados en el form
        context = self.get_context_data()
        formset_productos = context["productos"]

        # Pedido y productos son válidos
        if form.is_valid() and formset_productos.is_valid():

            # Pre guardado del pedido
            pedido = form.save(commit=False)

            # Asignar al usuario que guarda el formulario
            pedido.usuario = self.request.user

            # Calcular y sobreescribir el precio total del pedido
            pedido.precio_total = form.instance.precio_total

            # Guardar pedido
            pedido.save()

            formset_productos.instance = pedido
            formset_productos.save()

            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("pedidos:detail", kwargs={"pk": self.object.pk})


class PedidoUpdateView(SuccessMessageMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    # Modify the template used for this view
    template_name_suffix = "_update_form"
    success_message = "El pedido fue actualizado con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Le agregamos los productos al context para usarlos en el template
        if self.request.POST:
            context["productos"] = ProductosPedidoFormset(
                self.request.POST, instance=self.object
            )
        else:
            context["productos"] = ProductosPedidoFormset(instance=self.object)

            # Campo descuento como readonly si el usuario no tiene el permiso
            if not self.request.user.has_perm("pedidos.change_discount"):
                context["form"] = DescuentoSoloLecturaForm(instance=self.object)

        return context

    def form_valid(self, form):
        # Obtener info de pedido y productos posteados en el form
        context = self.get_context_data()
        formset_productos = context["productos"]

        # Pedido y productos son válidos
        if form.is_valid() and formset_productos.is_valid():

            # Pre guardado del pedido
            pedido = form.save(commit=False)

            # Calcular y sobreescribir el precio total del pedido
            pedido.precio_total = form.instance.precio_total

            # Guardar pedido
            pedido.save()

            formset_productos.instance = pedido
            formset_productos.save()

            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("pedidos:detail", kwargs={"pk": self.object.pk})


class PedidoDetailView(DetailView):
    model = Pedido

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        pedido: Pedido = self.get_object()

        descuento = pedido.get_precio_total * (pedido.descuento / 100)

        precio_final = pedido.get_precio_total - descuento

        context["precios"] = {
            "precio_final": precio_final,
            "descuento": descuento,
        }

        return context


class PedidoDeleteView(DeleteSuccessMessageMixin, DeleteView):
    model = Pedido
    success_url = reverse_lazy("pedidos:list")
    success_message = "El pedido fue eliminado con éxito."
