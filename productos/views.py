import django_tables2 as tables
from core.mixins import DeleteSuccessMessageMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.db.models import DecimalField, ExpressionWrapper
from django.db.models.expressions import F
from django.shortcuts import render
from django.template.defaultfilters import floatformat
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)
from django_filters import CharFilter, FilterSet, NumberFilter
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from variables.models import Variable

from .forms import InsumosProductoFormset, ProductoForm
from .models import Insumo, InsumosProducto, Producto, Unidad


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

        # v: Variable = Variable.objects.get(pk=1)
        # qs = Producto.objects \
        #     .select_related("insumo_base") \
        #     .select_related("insumo_lados") \
        #     .annotate(
        #         precioBase=(F('largo') / 100) * (F('ancho') / 100) * F('insumo_base__precio'),
        #         precioLatCorto=(F('ancho') / 100) * (F('alto') / 100),
        #         precioLatLargo=(F('largo') / 100) * (F('alto') / 100),
        #         horas=F('tiempo') / 60,
        #         precio_tiempo=F('horas') * v.precio_hora,
        #         precio_costo=ExpressionWrapper(F('precioBase') + F('precioLatCorto') + F('precioLatLargo') + F('precio_tiempo'), output_field=DecimalField()),
        #         precio_venta_crudo=F('precio_costo') * ((v.ganancia_por_menor / 100) + 1),
        #         tiempo_terminado=F('tiempo') * 2 / 60,
        #         precio_tiempo_terminado=F('tiempo_terminado') * v.precio_hora,
        #         precio_terminado=ExpressionWrapper(F('precio_costo') + v.precio_pintado + F('precio_tiempo_terminado'), output_field=DecimalField()),
        #         precio_venta_terminado=F('precio_terminado') * ((v.ganancia_por_menor / 100) + 1)
        #     )

        self.filter = self.filter_class(
            self.request.GET, queryset=super().get_table_data(),
        )
        return self.filter.qs

    def get_context_data(self, **kwargs):
        """ Inyecta el filtro en el context para usarlo en el template """
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filter
        return context


class ProductoCreateView(SuccessMessageMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/producto_form.html"
    success_message = "El producto fue creado con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Le agregamos los insumos al context para usarlos en el template
        if self.request.POST:
            context["insumos"] = InsumosProductoFormset(self.request.POST)
        else:
            context["insumos"] = InsumosProductoFormset()
        return context

    def form_valid(self, form):
        # Obtener info de producto e insumos posteados en el form
        context = self.get_context_data()
        formset_insumos = context["insumos"]

        # Guardar el Producto
        self.object = form.save()

        # Si son válidos los insumos se guardan
        if formset_insumos.is_valid():
            formset_insumos.instance = self.object
            formset_insumos.save()

            # Guardar producto completo
            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("productos:detail", kwargs={"pk": self.object.pk})


class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    success_message = "El producto fue actualizado con éxito."
    # Modify the template used for this view
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
        formset_insumos = context["insumos"]

        # Guardar producto
        self.object = form.save()

        if formset_insumos.is_valid():
            formset_insumos.instance = self.object
            formset_insumos.save()

            # Guardar producto completo
            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("productos:detail", kwargs={"pk": self.object.pk})


class ProductoDetailView(DetailView):
    model = Producto

    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     v: Variable = Variable.objects.get(pk=1)
    #     qs = queryset.annotate(
    #         precioBase=(F('largo') / 100) * (F('ancho') / 100) * F('insumo_base__precio'),
    #         precioLatCorto=(F('ancho') / 100) * (F('alto') / 100),
    #         precioLatLargo=(F('largo') / 100) * (F('alto') / 100),
    #         horas=F('tiempo') / 60,
    #         precio_tiempo=F('horas') * v.precio_hora,
    #         precio_costo=ExpressionWrapper(F('precioBase') + F('precioLatCorto') + F('precioLatLargo') + F('precio_tiempo'), output_field=DecimalField()),
    #         precio_venta_crudo=F('precio_costo') * ((v.ganancia_por_menor / 100) + 1),
    #         tiempo_terminado=F('tiempo') * 2 / 60,
    #         precio_tiempo_terminado=F('tiempo_terminado') * v.precio_hora,
    #         precio_terminado=ExpressionWrapper(F('precio_costo') + v.precio_pintado + F('precio_tiempo_terminado'), output_field=DecimalField()),
    #         precio_venta_terminado=F('precio_terminado') * ((v.ganancia_por_menor / 100) + 1)
    #     )

    #     return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(*args, **kwargs)
        return context


class ProductoDeleteView(DeleteSuccessMessageMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("productos:list")
    success_message = "El producto fue eliminado con éxito."
