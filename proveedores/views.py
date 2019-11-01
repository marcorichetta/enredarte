from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
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


class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedores/proveedores.html'
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
    success_url = 'proveedor'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        try:
            self.object.delete()
            # Redirect to success_url
        except ProtectedError:
            context = self.get_context_data(
                object=self.object,
                error=f'{self.object} no puede ser eliminado porque tiene dependencias'
            )
            return self.render_to_response(context)
        return HttpResponseRedirect(success_url)
