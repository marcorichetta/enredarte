from core.mixins import DeleteSuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from productos.forms import PrecioSoloLecturaForm
from productos.models import Irregular

from .forms import InsumosProductoFormset, ProductoIrregularForm


class ProductoIrregularCreateView(SuccessMessageMixin, CreateView):
    model = Irregular
    form_class = ProductoIrregularForm
    template_name = "productos/producto_form.html"
    success_message = "El producto fue creado con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Le agregamos los insumos al context para usarlos en el template
        if self.request.POST:
            context["insumos"] = InsumosProductoFormset(self.request.POST)
        else:
            context["insumos"] = InsumosProductoFormset()

            # Campo precio como readonly si el usuario no tiene el permiso
            if not self.request.user.has_perm("productos.change_product_price"):
                context["form"] = PrecioSoloLecturaForm()

        context["titulo"] = "Crear Producto Irregular"

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
        return reverse_lazy("productos:irregular:detail", kwargs={"pk": self.object.pk})


class ProductoIrregularUpdateView(SuccessMessageMixin, UpdateView):
    model = Irregular
    form_class = ProductoIrregularForm
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

            # Campo precio como readonly si el usuario no tiene el permiso
            if not self.request.user.has_perm("productos.change_product_price"):
                context["form"] = PrecioSoloLecturaForm(instance=self.object)

        context["titulo"] = "Actualizar Producto Irregular"

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
        return reverse_lazy("productos:irregular:detail", kwargs={"pk": self.object.pk})


class ProductoIrregularDetailView(PermissionRequiredMixin, DetailView):
    model = Irregular
    template_name = "productos/irregular_detail.html"

    permission_required = "productos.view_producto"


class ProductoIrregularDeleteView(DeleteSuccessMessageMixin, DeleteView):
    model = Irregular
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy("productos:list")
    success_message = "El producto fue eliminado con éxito."
