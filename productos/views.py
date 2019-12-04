from django.shortcuts import render
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

class ProductoCreateView(FormView):
    """ Armar views con un form de Producto y un formset para sus insumos
    (Falta validar y guardar todo en su lugar) """
    template_name = 'productos/producto_form.html'
    form_class = ProductoForm
    success_url = 'producto'

    def get_context_data(self, **kwargs):
        context = super(ProductoCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['insumos'] = InsumosProductoFormset(self.request.POST)
        else:
            context['insumos'] = InsumosProductoFormset()
        return context


class ProductoDetailView(DetailView):
    model = Producto

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(*args, **kwargs)
        return context

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = '__all__'

    # Modify the template used for this view
    template_name_suffix = '_update_form'


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = '/'
