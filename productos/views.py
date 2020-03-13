from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from .models import (
    Producto,
    Unidad,
    Insumo,
    InsumosProducto,
)

from extra_views import (
    CreateWithInlinesView,
    UpdateWithInlinesView,
    InlineFormSetFactory,
)

from .forms import ProductoForm, InsumosProductoFormset
from django.db import transaction

# Create your views here.

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/productos.html'
    context_object_name = 'productos'
    ordering = ['id']
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ProductoListView, self).get_queryset()

        # Permite buscar en un form dentro de la misma página
        # con el formato q?<nombre-del-producto>
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)
        return queryset


""" class InsumosProductoInline(InlineFormSetFactory):
    model = InsumosProducto
    fields = ['insumo', 'cantidad']
    factory_kwargs = {'extra': 3, 'max_num': 5, 'can_delete': False}

class ProductoCreateView(CreateWithInlinesView):
    model = Producto
    inlines = [
        InsumosProductoInline
        ]
    fields = '__all__'
    template_name = 'productos/producto_form.html' """

class ProductoCreateView(CreateView):
    """ Armar views con un form de Producto y un formset para sus insumos
    (Falta validar y guardar todo en su lugar) """
    model = Producto
    template_name = 'productos/producto_form.html'
    form_class = ProductoForm

    def get_context_data(self, **kwargs):
        context = super(ProductoCreateView, self).get_context_data(**kwargs)
        # Le agregamos los insumos al context para usarlos en el template
        if self.request.POST:
            context['insumos'] = InsumosProductoFormset(self.request.POST)
        else:
            context['insumos'] = InsumosProductoFormset()
        return context

    def form_valid(self, form):
        # Obtener info de producto e insumos posteados en el form
        context = self.get_context_data()
        insumos = context['insumos']

        # Esto se ejecuta sólo si la transacción es atómica
        # https://docs.djangoproject.com/en/2.1/topics/db/transactions/#controlling-transactions-explicitly
        with transaction.atomic():
            # Guardar el Producto
            self.object = form.save()
            # Si son válidos los insumos se guardan
            if insumos.is_valid():
                insumos.instance = self.object
                insumos.save()

                # Guardar producto completo
                return super(ProductoCreateView, self).form_valid(form)
            else:
                # Repopular form con errores
                return self.render_to_response(self.get_context_data(form=form))


    def get_success_url(self):
        return reverse_lazy('detailProducto', kwargs={'pk': self.object.pk})


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    #template_name = 'productos/producto_form.html'
    # Modify the template used for this view
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super(ProductoUpdateView, self).get_context_data(**kwargs)

        # Enviar el objeto como instancia para ser actualizado
        if self.request.POST:
            context['insumos'] = InsumosProductoFormset(self.request.POST, instance=self.object)
        else:
            context['insumos'] = InsumosProductoFormset(instance=self.object)
        return context

    def form_valid(self, form):
        # Obtenemos info de producto e insumos posteados en el form
        context = self.get_context_data()
        insumos = context['insumos']

        # Esto se ejecuta sólo si la transacción es atómica
        # https://docs.djangoproject.com/en/2.1/topics/db/transactions/#controlling-transactions-explicitly
        with transaction.atomic():
            self.object = form.save()
            if insumos.is_valid():
                insumos.instance = self.object
                insumos.save()
                # Guardar producto completo
                return super(ProductoUpdateView, self).form_valid(form)
            else:
                # Repopular form con errores
                return self.render_to_response(self.get_context_data(form=form))


    def get_success_url(self):
        return reverse_lazy('detailProducto', kwargs={'pk': self.object.pk})


class ProductoDetailView(DetailView):
    model = Producto

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(*args, **kwargs)
        return context


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = '/productos/'
