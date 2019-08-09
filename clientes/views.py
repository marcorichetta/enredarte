from django.shortcuts import render
from django.db.models import Q

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from .models import Cliente
# Create your views here.

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/clientes.html'
    context_object_name = 'clientes'
    ordering = ['id']
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ClienteListView, self).get_queryset()

        # Permite buscar en un form dentro de la misma página
        # con el formato q?<nombre-del-producto>
        query = self.request.GET.get("q")
        if query:
            return queryset.filter(
                Q(nombre__icontains=query) |
                Q(apellido__icontains=query) |
                Q(email__icontains=query)
            )
        return queryset

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'telefono', 'email',
              'calle', 'numero', 'localidad']


class ClienteDetailView(DetailView):
    model = Cliente


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'

    # Modify the template used for this view
    template_name_suffix = '_update_form'


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = '/'
