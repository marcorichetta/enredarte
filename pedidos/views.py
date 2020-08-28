from django.http import HttpResponseRedirect
from django.db.models import ProtectedError, Q
from django.contrib import messages
from django.db import transaction

from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Pedido
from .forms import PedidoForm, ProductosPedidoFormset

# Create your views here.


class PedidoListView(ListView):
    model = Pedido
    template_name = "pedidos/pedidos.html"
    context_object_name = "pedidos"
    ordering = ["id"]
    paginate_by = 10

    def get_queryset(self):
        """ Permite buscar en un form dentro de la misma página
        con el formato `q?texto` """
        queryset = super(PedidoListView, self).get_queryset()

        query = self.request.GET.get("search")
        if query:
            return queryset.filter(
                Q(cliente__nombre__icontains=query) | Q(cliente__nombre__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        """ Devuelve el texto buscado para usarlo en la paginación """
        context = super(PedidoListView, self).get_context_data(**kwargs)
        context["search_txt"] = self.request.GET.get("search", "")
        return context


class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    success_message = "Pedido %(pk)s fue creado correctamente"

    def get_context_data(self, **kwargs):
        context = super(PedidoCreateView, self).get_context_data(**kwargs)
        # Le agregamos los productos al context para usarlos en el template
        if self.request.POST:
            context["productos"] = ProductosPedidoFormset(self.request.POST)
        else:
            context["productos"] = ProductosPedidoFormset()
        return context

    def form_valid(self, form):
        # Obtener info de pedido y productos posteados en el form
        context = self.get_context_data()
        formset_productos = context["productos"]

        # Pre guardado del pedido
        nuevo_pedido = form.save(commit=False)

        # Calcular y sobreescribir el precio total del pedido
        nuevo_pedido.precio_total = form.instance.get_precio_total

        # Si son válidos los productos se guardan
        if formset_productos.is_valid():
            # Guardar pedido
            nuevo_pedido.save()

            formset_productos.instance = nuevo_pedido
            formset_productos.save()

            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))


class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    # Modify the template used for this view
    template_name_suffix = "_update_form"
    success_message = "Pedido %(pk)s fue actualizado correctamente"

    def get_context_data(self, **kwargs):
        context = super(PedidoUpdateView, self).get_context_data(**kwargs)
        # Le agregamos los productos al context para usarlos en el template
        if self.request.POST:
            context["productos"] = ProductosPedidoFormset(
                self.request.POST, instance=self.object
            )
        else:
            context["productos"] = ProductosPedidoFormset(instance=self.object)
        return context

    def form_valid(self, form):
        # Obtener info de pedido y productos posteados en el form
        context = self.get_context_data()
        formset_productos = context["productos"]

        # Pre guardar el pedido
        pedido_actualizado = form.save(commit=False)

        # Calcular y sobreescribir el precio total del pedido
        pedido_actualizado.precio_total = form.instance.get_precio_total

        # Si son válidos los productos se guardan
        if formset_productos.is_valid():
            # Guardar pedido
            pedido_actualizado.save()

            formset_productos.instance = pedido_actualizado
            formset_productos.save()

            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("detailPedido", kwargs={"pk": self.object.pk})


class PedidoDetailView(DetailView):
    model = Pedido

    def get_context_data(self, *args, **kwargs):
        context = super(PedidoDetailView, self).get_context_data(*args, **kwargs)
        return context


class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = reverse_lazy("pedido")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        try:
            self.object.delete()
            # Enviar mensaje para mostrar alerta
            messages.success(request, f"Pedido {kwargs.get('pk')} fue eliminado.")

            # Redirect to success_url
        except ProtectedError:
            context = self.get_context_data(
                object=self.object,
                error=f"{self.object} no puede ser eliminado porque \
                    tiene dependencias. Consulte al administrador.",
            )
            return self.render_to_response(context)
        return HttpResponseRedirect(success_url)
