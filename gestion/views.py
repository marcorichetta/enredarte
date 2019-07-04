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
    exclude = ['detalles']
    fields = ['razon_social', 'cuit', 'telefono', 'email',
              'calle', 'numero', 'localidad']


class ProveedorDetailView(DetailView):
    model = Proveedor


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = '__all__'


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    success_url = '/'
