from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Proveedor
# Create your views here.


@login_required
def index(request):

    return render(request, 'gestion/index.html')

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'gestion/proveedores.html'
    context_object_name = 'proveedores'
    ordering = ['razon_social']
    paginate_by = 3


class ProveedorCreateView(CreateView):
    model = Proveedor
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
