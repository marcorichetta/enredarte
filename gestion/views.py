from django.http import JsonResponse, HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from pedidos.models import Pedido
from clientes.models import Cliente
from productos.models import Producto

from .models import Localidad, Provincia

# Create your views here.


class Dashboard(LoginRequiredMixin, TemplateView):
    """ Panel principal que contiene información útil para el usuario """

    template_name = "gestion/index.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context["pedidos"] = Pedido.objects.get_queryset()[:5]
        context["clientes"] = Cliente.objects.get_queryset()
        context["productos"] = Producto.objects.get_queryset()[:5]

        context["estados_pedidos"] = Pedido.ESTADO_PEDIDO_CHOICES

        return context


@require_http_methods(["POST"])
def LocalidadCreate(request):
    cod_postal = request.POST.get("cod_postal")
    localidad = request.POST.get("localidad")
    provincia_id = request.POST.get("provincia_id")

    # Obtener instancia de Provincia
    provincia = Provincia.objects.get(pk=provincia_id)

    # Crear en DB
    Localidad.objects.create(cod_postal=cod_postal, localidad=localidad, provincia=provincia)

    # Enviar dict con datos de la nueva Localidad
    nuevaLocalidad = {"cod_postal": cod_postal, "localidad": localidad, "provincia": provincia_id}

    # Devolver info a JS
    return JsonResponse(nuevaLocalidad)