from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError, Q
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import Proveedor

# Create your views here.


class ProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedores/proveedores.html"
    context_object_name = "proveedores"
    ordering = ["id"]
    paginate_by = 10

    def get_queryset(self):
        """ Permite buscar en un form dentro de la misma página
        con el formato `q?texto` """
        queryset = super(ProveedorListView, self).get_queryset()

        query = self.request.GET.get("search")
        if query:
            return queryset.filter(Q(razon_social__icontains=query))
        return queryset

    def get_context_data(self, **kwargs):
        """ Devuelve el texto buscado para usarlo en la paginación """
        context = super(ProveedorListView, self).get_context_data(**kwargs)
        context["search_txt"] = self.request.GET.get("search", "")
        return context


class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = ["cuit", "razon_social", "telefono", "email", "calle", "numero", "localidad"]


class ProveedorDetailView(DetailView):
    model = Proveedor


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = "__all__"

    # Modify the template used for this view
    template_name_suffix = "_update_form"


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    success_url = reverse_lazy("proveedores:list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        try:
            self.object.delete()
            # Enviar mensaje para mostrar alerta
            messages.success(request, f"{self.object} fue eliminado.")

            # Redirect to success_url
        except ProtectedError:
            context = self.get_context_data(
                object=self.object,
                error=f"{self.object} no puede ser eliminado porque \
                    tiene dependencias. Consulte al administrador.",
            )
            return self.render_to_response(context)
        return HttpResponseRedirect(success_url)
