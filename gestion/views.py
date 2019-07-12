from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from .models import Proveedor, Cliente
# Create your views here.


@login_required
def index(request):

    return render(request, 'gestion/index.html')


class GeneralListView(TemplateView):
    
    template_name = "gestion/index.html"

    def get_context_data(self, **kwargs):
        context = super(GeneralListView, self).get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        context['proveedores'] = Proveedor.objects.get_queryset()
        return context
    


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
