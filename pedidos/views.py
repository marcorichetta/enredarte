from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from .models import Pedido
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


class PedidoCreateView(CreateView):
    model = Pedido
    fields = '__all__'

class PedidoDetailView(DetailView):
    model = Pedido

class PedidoUpdateView(UpdateView):
    model = Pedido
    fields = '__all__'

    # Modify the template used for this view
    template_name_suffix = '_update_form'

class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = '/'
