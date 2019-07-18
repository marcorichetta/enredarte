from django.shortcuts import render

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
