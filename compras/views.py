from django.shortcuts import render
from django.db.models import Q

from django.views.generic import (
    ListView,
)

from .models import Compra, InsumosCompra

# Create your views here.

class CompraListView(ListView):
    model = Compra
    template_name = 'compras/compras.html'
    context_object_name = 'compras'
    ordering = ['id']
    paginate_by = 10

    def get_queryset(self):
        queryset = super(CompraListView, self).get_queryset()

        # Permite buscar en un form dentro de la misma página
        # con el formato q?<nombre-del-producto>
        query = self.request.GET.get("q")
        if query:
            return queryset.filter(
                Q(proveedor__razon_social__icontains=query))
        return queryset
