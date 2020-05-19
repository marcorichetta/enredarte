from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError
from django.contrib import messages
from django.db import transaction

from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from .models import Pedido, ProductosPedido
from .forms import PedidoForm, ProductosPedidoFormset

# Create your views here.


class PedidoListView(ListView):
    model = Pedido
    template_name = "pedidos/pedidos.html"
    context_object_name = "pedidos"
    ordering = ["id"]
    paginate_by = 10

    def get_queryset(self):
        queryset = super(PedidoListView, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)
        return queryset


class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm

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
        productos = context["productos"]

        # Esto se ejecuta sólo si la transacción es atómica
        # https://docs.djangoproject.com/en/2.1/topics/db/transactions/#controlling-transactions-explicitly
        with transaction.atomic():
            # Guardar la compra
            self.object = form.save()
            # Si son válidos los productos se guardan
            if productos.is_valid():
                productos.instance = self.object
                productos.save()

                # Guardar compra completa
                return super(PedidoCreateView, self).form_valid(form)

            # Repopular form con errores
            return self.render_to_response(self.get_context_data(form=form))


class PedidoUpdateView(UpdateView):
    model = Pedido
    fields = ["cliente", "precio_final", "detalles", "estado"]
    template_name = "pedidos/pedido_update_form.html"


class PedidoDetailView(DetailView):
    model = Pedido


class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = reverse_lazy("pedido")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        try:
            self.object.delete()
            # Enviar mensaje para mostrar alerta
            messages.success(request, f"{self.object} fue eliminado.")

            # Redirect to success_url
        except ProtectedError:
            context = self.get_context_data(
                object=self.object,
                error=f"{self.object} no puede ser eliminado porque \
                    tiene dependencias. Consulte al administrador.",
            )
            return self.render_to_response(context)
        return HttpResponseRedirect(success_url)
