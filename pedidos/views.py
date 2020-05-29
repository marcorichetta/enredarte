from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import ProtectedError, Q
from django.contrib import messages
from django.db import transaction

from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from .models import Pedido, ProductosPedido
from .forms import PedidoForm, ProductosPedidoFormset

# Create your views here.


class PedidoListView(ListView):
    model = Pedido
    template_name = "pedidos/pedidos.html"
    context_object_name = "pedidos"
    ordering = ["id"]
    paginate_by = 10

    def get_queryset(self):
        """ Permite buscar en un form dentro de la misma página
        con el formato `q?texto` """
        queryset = super(PedidoListView, self).get_queryset()

        query = self.request.GET.get("search")
        if query:
            return queryset.filter(
                Q(cliente__nombre__icontains=query) | Q(cliente__nombre__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        ''' Devuelve el texto buscado para usarlo en la paginación '''
        context = super(PedidoListView, self).get_context_data(**kwargs)
        context["search_txt"] = self.request.GET.get("search", "")
        return context


class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    success_message = "Pedido %(pk)s fue creado correctamente"

    def get_context_data(self, **kwargs):
        context = super(PedidoCreateView, self).get_context_data(**kwargs)
        # Le agregamos los productos al context para usarlos en el template
        if self.request.POST:
            context["productos"] = ProductosPedidoFormset(self.request.POST)
        else:
            context["productos"] = ProductosPedidoFormset()
        return context

    def form_valid(self, form):
        # Obtener info de pedido y productos posteados en el form
        context = self.get_context_data()
        productos = context["productos"]

        # Esto se ejecuta sólo si la transacción es atómica
        # https://docs.djangoproject.com/en/2.1/topics/db/transactions/#controlling-transactions-explicitly
        with transaction.atomic():
            # Guardar el pedido
            self.object = form.save()
            # Si son válidos los productos se guardan
            if productos.is_valid():
                productos.instance = self.object
                productos.save()

                # Guardar pedido completa
                return super(PedidoCreateView, self).form_valid(form)

            # Repopular form con errores
            return self.render_to_response(self.get_context_data(form=form))


class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    # Modify the template used for this view
    template_name_suffix = "_update_form"
    success_message = "Pedido %(pk)s fue actualizado correctamente"

    def get_context_data(self, **kwargs):
        context = super(PedidoUpdateView, self).get_context_data(**kwargs)
        # Le agregamos los productos al context para usarlos en el template
        if self.request.POST:
            context["productos"] = ProductosPedidoFormset(self.request.POST)
        else:
            context["productos"] = ProductosPedidoFormset(instance=self.object)
        return context

    def form_valid(self, form):
        # Obtener info de pedido y productos posteados en el form
        context = self.get_context_data()
        productos = context["productos"]

        # Esto se ejecuta sólo si la transacción es atómica
        # https://docs.djangoproject.com/en/2.1/topics/db/transactions/#controlling-transactions-explicitly
        with transaction.atomic():
            # Guardar el pedido
            self.object = form.save()
            # Si son válidos los productos se guardan
            if productos.is_valid():
                productos.instance = self.object
                productos.save()

                # Guardar pedido completa
                return super(PedidoUpdateView, self).form_valid(form)

            # Repopular form con errores
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("detailPedido", kwargs={"pk": self.object.pk})


class PedidoDetailView(DetailView):
    model = Pedido

    def get_context_data(self, *args, **kwargs):
        context = super(PedidoDetailView, self).get_context_data(*args, **kwargs)
        return context


class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = reverse_lazy("pedido")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        try:
            self.object.delete()
            # Enviar mensaje para mostrar alerta
            messages.success(request, f"Pedido {kwargs.get('pk')} fue eliminado.")

            # Redirect to success_url
        except ProtectedError:
            context = self.get_context_data(
                object=self.object,
                error=f"{self.object} no puede ser eliminado porque \
                    tiene dependencias. Consulte al administrador.",
            )
            return self.render_to_response(context)
        return HttpResponseRedirect(success_url)

@require_http_methods(["GET"])
def get_pedidos(request):
    '''
        Vista llamada al inicializar el calendario.
        
        Devuelve los pedidos pendientes de entrega
    '''

    pedidos = Pedido.objects.all()

    pedidos = [{
        'id': p.id,
        'title': str(p.cliente),
        'start': p.fecha_pedido.isoformat(),
        'status': p.estado,
    } for p in pedidos]

    return JsonResponse(pedidos, safe=False)