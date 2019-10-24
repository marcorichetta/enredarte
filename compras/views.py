from django.shortcuts import render
from django.http import HttpResponseRedirect
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

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)
        return queryset