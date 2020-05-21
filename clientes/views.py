from django.shortcuts import HttpResponseRedirect
from django.db.models import Q
from django.db.models import ProtectedError
from django.contrib import messages
from django.urls import reverse_lazy


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from gestion.models import Provincia, Localidad
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
        ''' Devuelve el texto buscado para usarlo en la paginación '''
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context["search_txt"] = self.request.GET.get("search", "")
        return context


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "telefono", "email", "calle", "numero", "localidad"]

    def get_context_data(self, **kwargs):
        context = super(ClienteCreateView, self).get_context_data(**kwargs)

        # Devuelve una lista con los id y los nombres de localidades y provincias
        # Se usan en el form original y en el modal para crear nueva localidad
        context["localidades"] = Localidad.objects.get_queryset()
        context["provincias"] = Provincia.objects.get_queryset()

        return context


class ClienteDetailView(DetailView):
    model = Cliente


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = "__all__"

    # Modify the template used for this view
    template_name_suffix = "_update_form"


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("cliente")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        try:
            self.object.delete()
            # Enviar mensaje para mostrar alerta
            messages.success(request, f"El cliente {self.object} fue eliminado.")

            # Redirect to success_url
        except ProtectedError:
            context = self.get_context_data(
                object=self.object,
                error=f"{self.object} no puede ser eliminado porque \
                    tiene dependencias. Consulte al administrador.",
            )
            return self.render_to_response(context)
        return HttpResponseRedirect(success_url)
