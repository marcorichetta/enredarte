from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from proveedores.models import Proveedor
from pedidos.models import Pedido
from clientes.models import Cliente

# Create your views here.


class Dashboard(LoginRequiredMixin, TemplateView):
    """ Panel principal que contiene información útil para el usuario """

    template_name = "gestion/index.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['pedidos'] = Pedido.objects.get_queryset()[:5]
        context['clientes'] = Cliente.objects.get_queryset()
        return context
