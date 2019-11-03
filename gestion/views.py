from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    CreateView,
    FormView
)
from proveedores.models import Proveedor
from pedidos.models import Pedido
from clientes.models import Cliente

from .models import Localidad, Provincia

# Create your views here.


class Dashboard(LoginRequiredMixin, TemplateView):
    """ Panel principal que contiene información útil para el usuario """

    template_name = "gestion/index.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['pedidos'] = Pedido.objects.get_queryset()[:5]
        context['clientes'] = Cliente.objects.get_queryset()
        return context


def LocalidadCreate(request):
    if request.method == "POST":
        cod_postal = request.POST['cod_postal']
        localidad = request.POST['localidad']
        provincia_id = request.POST['provincia']

        # Obtener instancia de Provincia
        provincia = Provincia.objects.get(pk=provincia_id)

        # Crear en DB
        Localidad.objects.create(
            cod_postal=cod_postal,
            localidad=localidad,
            provincia=provincia
        )

        # Enviar dict con datos de la nueva Localidad
        nuevaLocalidad = {
            'cod_postal': cod_postal,
            'localidad': localidad,
            'provincia': provincia_id
        }

        # Devolver info a JS
        return JsonResponse(nuevaLocalidad)


class ViewPrueba(FormView):
    template_name = 'gestion/prueba_select2.html'
