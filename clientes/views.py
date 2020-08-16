from django.shortcuts import HttpResponseRedirect
from django.db.models import Q
from django.db.models import ProtectedError
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core.models import Provincia, Localidad
from .models import Cliente


class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/clientes.html"
    context_object_name = "clientes"
    ordering = ["id"]
    paginate_by = 10

    def get_queryset(self):
        """ Permite buscar en un form dentro de la misma página
        con el formato `q?texto` """

        queryset = super(ClienteListView, self).get_queryset()
        query = self.request.GET.get("q")
        if query:
            return queryset.filter(
                Q(nombre__icontains=query)
                | Q(apellido__icontains=query)
                | Q(email__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        """ Devuelve el texto buscado para usarlo en la paginación """
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context["search_txt"] = self.request.GET.get("search", "")
        return context


class ClienteCreateView(SuccessMessageMixin, CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "telefono", "email", "calle", "numero", "localidad"]
    success_message = "Creado con éxito."

    def get_context_data(self, **kwargs):
        context = super(ClienteCreateView, self).get_context_data(**kwargs)

        # Devuelve una lista con los id y los nombres de localidades y provincias
        # Se usan en el form original y en el modal para crear nueva localidad
        context["localidades"] = Localidad.objects.get_queryset()
        context["provincias"] = Provincia.objects.get_queryset()

        return context


class ClienteDetailView(DetailView):
    model = Cliente


class ClienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Cliente
    fields = [
        "nombre",
        "apellido",
        "telefono",
        "email",
        "calle",
        "numero",
        "localidad",
        "detalles",
    ]
    success_message = "Actualizado con éxito."

    # Modify the template used for this view
    template_name_suffix = "_update_form"


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("cliente")
