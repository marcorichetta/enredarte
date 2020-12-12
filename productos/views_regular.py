from core.mixins import DeleteSuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from variables.models import Variable

from productos.models import Regular

from .forms import InsumosProductoFormset, ProductoRegularForm


class ProductoRegularCreateView(SuccessMessageMixin, CreateView):
    model = Regular
    form_class = ProductoRegularForm
    template_name = "productos/producto_form.html"
    success_message = "El producto fue creado con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Le agregamos los insumos al context para usarlos en el template
        if self.request.POST:
            context["insumos"] = InsumosProductoFormset(self.request.POST)
        else:
            context["insumos"] = InsumosProductoFormset()

        context["titulo"] = "Crear Producto Regular"

        return context

    def form_valid(self, form):
        # Obtener info de producto e insumos posteados en el form
        context = self.get_context_data()
        formset_insumos = context["insumos"]

        # Producto e insumos son válidos
        if form.is_valid() and formset_insumos.is_valid():

            # Guardar el Producto
            self.object = form.save()

            formset_insumos.instance = self.object
            formset_insumos.save()

            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("productos:regular:detail", kwargs={"pk": self.object.pk})


class ProductoRegularUpdateView(SuccessMessageMixin, UpdateView):
    model = Regular
    form_class = ProductoRegularForm
    success_message = "El producto fue actualizado con éxito."
    template_name = "productos/producto_update_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Enviar el objeto como instancia para ser actualizado
        if self.request.POST:
            context["insumos"] = InsumosProductoFormset(
                self.request.POST, instance=self.object
            )
        else:
            context["insumos"] = InsumosProductoFormset(instance=self.object)

        context["titulo"] = "Actualizar Producto Regular"

        return context

    def form_valid(self, form):
        # Obtenemos info de producto e insumos posteados en el form
        context = self.get_context_data()
        formset_insumos = context["insumos"]

        # Producto e insumos son válidos
        if form.is_valid() and formset_insumos.is_valid():

            # Guardar el Producto
            self.object = form.save()

            formset_insumos.instance = self.object
            formset_insumos.save()

            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("productos:regular:detail", kwargs={"pk": self.object.pk})


class ProductoRegularDetailView(PermissionRequiredMixin, DetailView):
    model = Regular
    template_name = "productos/regular_detail.html"

    permission_required = "productos.view_producto"

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
        context = super().get_context_data(*args, **kwargs)

        prod: Regular = self.get_object()
        var: Variable = Variable.objects.get(pk=1)

        context["precios"] = {
            "precio_costo": prod.precio_costo(variables=var),
            "precio_venta_crudo": prod.precio_venta_crudo(),
            "precio_terminado": prod.precio_terminado(variables=var),
        }

        return context


class ProductoRegularDeleteView(DeleteSuccessMessageMixin, DeleteView):
    model = Regular
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy("productos:list")
    success_message = "El producto fue eliminado con éxito."
