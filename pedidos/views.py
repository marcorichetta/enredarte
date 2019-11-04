from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from .models import Pedido, ProductosPedido
from extra_views import (
    CreateWithInlinesView,
    UpdateWithInlinesView,
    InlineFormSetFactory,
)

# Create your views here.

class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedidos/pedidos.html'
    context_object_name = 'pedidos'
    ordering = ['id']
    paginate_by = 10

    def get_queryset(self):
        queryset = super(PedidoListView, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)
        return queryset

class ProductosPedidoInline(InlineFormSetFactory):
    model = ProductosPedido
    fields = ['producto', 'cantidad']
    factory_kwargs = {'extra': 3, 'max_num': 5, 'can_delete': False}

class PedidoCreateView(CreateWithInlinesView):
    model = Pedido
    inlines = [ProductosPedidoInline]
    fields = ['id', 'cliente', 'precio_final', 'detalles', 'estado']
    template_name = 'pedidos/pedido_form.html'

class PedidoUpdateView(UpdateWithInlinesView):
    model = Pedido
    inlines = [ProductosPedidoInline]
    fields = ['cliente', 'precio_final', 'detalles', 'estado']
    template_name = 'pedidos/pedido_update_form.html'


class PedidoDetailView(DetailView):
    model = Pedido

class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedido')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        try:
            self.object.delete()
            # Enviar mensaje para mostrar alerta
            messages.success(
                request, f'{self.object} fue eliminado.')

            # Redirect to success_url
        except ProtectedError:
            context = self.get_context_data(
                object=self.object,
                error=f'{self.object} no puede ser eliminado porque \
                    tiene dependencias. Consulte al administrador.',
            )
            return self.render_to_response(context)
        return HttpResponseRedirect(success_url)
