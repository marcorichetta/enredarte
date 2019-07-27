from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Producto, Unidad, Insumo, InsumosProducto, Variante

from .forms import InsumosProductoFormset, VarianteFormSet
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

class VarianteListView(ListView):
    model = Variante
    template_name = 'productos/variantes.html'
    context_object_name = 'variantes'
    ordering = ['id']

    def get_queryset(self, *args, **kwargs):
        return Variante.objects.filter(producto_id=self.kwargs.get('pk'))

class VarianteCreateView(CreateView):
    model = Variante
    fields = '__all__'

    """ def get_context_data(self, *args, **kwargs):
        context = super(VarianteCreateView, self).get_context_data(*args, **kwargs)
        context['formset'] = VarianteFormSet(queryset=self.get_queryset())
        return context """

    

class ProductoCreateView(CreateView):
    model = Producto
    fields = '__all__'
    exclude = ['insumos']
    
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


""" Armar views con un form de Producto y un formset para sus insumos
    (Falta validar y guardar todo en su lugar)

    class ProductoView(FormView):
    template_name = 'productos/producto_test.html'
    form_class = ProductoForm
    success_url = 'producto'

    def get_context_data(self, **kwargs):
        context = super(ProductoView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['insumos'] = InsumosProductoFormset(self.request.POST)
        else:
            context['insumos'] = InsumosProductoFormset()
        return context """
