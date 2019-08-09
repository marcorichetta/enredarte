from django.shortcuts import render
from django.http import HttpResponseRedirect
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
    success_url = '/'
