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
from .models import Proveedor
# Create your views here.


class Dashboard(LoginRequiredMixin, TemplateView):
    """ Panel principal que contiene información útil para el usuario """

    template_name = "gestion/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['proveedores'] = Proveedor.objects.get_queryset()
        return context


class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'gestion/proveedores.html'
    context_object_name = 'proveedores'
    ordering = ['id']
    paginate_by = 10

    def get_queryset(self):
        """ Override queryset method to be able to respond
            to search forms in proveedores.html """
        queryset = super(ProveedorListView, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(razon_social__icontains=q)
        return queryset

class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = ['cuit', 'razon_social', 'telefono', 'email',
              'calle', 'numero', 'localidad']


class ProveedorDetailView(DetailView):
    model = Proveedor


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = '__all__'

    # Modify the template used for this view
    template_name_suffix = '_update_form'


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    success_url = '/'
