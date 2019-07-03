from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Proveedor
# Create your views here.

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'gestion/index.html'
    context_object_name = 'proveedores'
    ordering = ['razon_social']
    paginate_by = 2

class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = ['razon_social', 'cuit', 'telefono', 'email']

class ProveedorDetailView(DetailView):
    model = Proveedor

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = ['razon_social', 'cuit', 'telefono', 'email', 'detalles']

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    success_url = '/'
