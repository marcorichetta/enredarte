from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
from .models import Producto, Unidad, Insumo, InsumosProducto

from .forms import ProductoForm, InsumosProductoFormset
from django.db import transaction

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from django_filters import FilterSet, CharFilter, NumberFilter
from django_filters.views import FilterView
from django.template.defaultfilters import floatformat


class ProductoTable(tables.Table):
    class Meta:
        model = Producto
        fields = (
            "id",
            "nombre",
            "insumo_base",
            "insumo_lados",
            "precio_venta_terminado",
            "opciones",
        )
        attrs = {"class": "table table-sm table-hover"}
        order_by = "id"

    def render_precio_venta_terminado(self, value):
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
    )


class ProductoFilter(FilterSet):
    nombre = CharFilter(
        field_name="nombre", lookup_expr="icontains", label="Buscar por nombre"
    )

    class Meta:
        model = Producto
        fields = ["nombre"]


class ProductoListView(ExportMixin, tables.SingleTableView):
    table_class = ProductoTable
    model = Producto
    filter_class = ProductoFilter
    template_name = "productos/productos.html"
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
            self.request.GET, queryset=super().get_table_data()
        )
        return self.filter.qs

    def get_context_data(self, **kwargs):
        """ Devuelve el texto buscado para usarlo en la paginación """
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filter
        return context


class ProductoCreateView(CreateView):
    """ Armar views con un form de Producto y un formset para sus insumos
    (Falta validar y guardar todo en su lugar) """

    model = Producto
    template_name = "productos/producto_form.html"
    form_class = ProductoForm

    def get_context_data(self, **kwargs):
        context = super(ProductoCreateView, self).get_context_data(**kwargs)
        # Le agregamos los insumos al context para usarlos en el template
        if self.request.POST:
            context["insumos"] = InsumosProductoFormset(self.request.POST)
        else:
            context["insumos"] = InsumosProductoFormset()
        return context

    def form_valid(self, form):
        # Obtener info de producto e insumos posteados en el form
        context = self.get_context_data()
        insumos = context["insumos"]

        # Esto se ejecuta sólo si la transacción es atómica
        # https://docs.djangoproject.com/en/2.1/topics/db/transactions/#controlling-transactions-explicitly
        with transaction.atomic():
            # Guardar el Producto
            self.object = form.save()
            # Si son válidos los insumos se guardan
            if insumos.is_valid():
                insumos.instance = self.object
                insumos.save()

                # Guardar producto completo
                return super(ProductoCreateView, self).form_valid(form)
            else:
                # Repopular form con errores
                return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("productos:detail", kwargs={"pk": self.object.pk})


class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    success_message = "Producto actualizado con éxito."
    # Modify the template used for this view
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super(ProductoUpdateView, self).get_context_data(**kwargs)

        # Enviar el objeto como instancia para ser actualizado
        if self.request.POST:
            context["insumos"] = InsumosProductoFormset(
                self.request.POST, instance=self.object
            )
        else:
            context["insumos"] = InsumosProductoFormset(instance=self.object)
        return context

    def form_valid(self, form):
        # Obtenemos info de producto e insumos posteados en el form
        context = self.get_context_data()
        insumos = context["insumos"]

        # Esto se ejecuta sólo si la transacción es atómica
        # https://docs.djangoproject.com/en/2.1/topics/db/transactions/#controlling-transactions-explicitly
        with transaction.atomic():
            self.object = form.save()
            if insumos.is_valid():
                insumos.instance = self.object
                insumos.save()
                # Guardar producto completo
                return super(ProductoUpdateView, self).form_valid(form)
            else:
                # Repopular form con errores
                return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("productos:detail", kwargs={"pk": self.object.pk})


class ProductoDetailView(DetailView):
    model = Producto

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(*args, **kwargs)
        return context


class ProductoDeleteView(SuccessMessageMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("productos:list")
    success_message = "Eliminado con éxito."
