from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Producto

from .forms import ProductoForm, InsumosProductoFormset, ProductImageFormset

# Create your views here.


class ProductoListView(ListView):
    model = Producto
    template_name = "productos/productos.html"
    context_object_name = "productos"
    ordering = ["id"]
    paginate_by = 10

    def get_queryset(self):
        """ Permite buscar en un form dentro de la misma página
        con el formato `q?texto` """
        queryset = super().get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)
        return queryset

    def get_context_data(self, **kwargs):
        """ Devuelve el texto buscado para usarlo en la paginación """
        context = super().get_context_data(**kwargs)
        context["search_txt"] = self.request.GET.get("search", "")
        return context


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
    template_name = "productos/producto_form.html"
    form_class = ProductoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            # En caso de estar guardando un producto instanciamos los formsets
            context["insumos"] = InsumosProductoFormset(self.request.POST)
            context["imagenes"] = ProductImageFormset(
                self.request.POST, self.request.FILES,
            )
        else:
            # Incluímos los formsets al context para usarlos en el template
            context["insumos"] = InsumosProductoFormset()
            context["imagenes"] = ProductImageFormset()
        return context

    def form_valid(self, form):
        # Obtener info de producto e imágenes enviados en el form
        context = self.get_context_data()
        formset_insumos = context["insumos"]
        formset_imagenes = context["imagenes"]

        # Guardar el Producto
        self.object = form.save()

        # Si son válidos las imágenes se guardan
        if formset_insumos.is_valid() and formset_imagenes.is_valid():
            formset_insumos.instance = self.object
            formset_insumos.save()

            formset_imagenes.instance = self.object
            formset_imagenes.save()

            # Guardar producto completo
            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("productos:detail", kwargs={"pk": self.object.pk})


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    # Modify the template used for this view
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super(ProductoUpdateView, self).get_context_data(**kwargs)

        # Enviar el objeto como instancia para ser actualizado
        if self.request.POST:
            context["insumos"] = InsumosProductoFormset(
                self.request.POST, instance=self.object
            )
            context["imagenes"] = ProductImageFormset(
                self.request.POST, self.request.FILES, instance=self.object
            )

        else:
            context["insumos"] = InsumosProductoFormset(instance=self.object)
            context["imagenes"] = ProductImageFormset(instance=self.object)
        return context

    def form_valid(self, form):
        # Obtenemos info de producto e insumos posteados en el form
        context = self.get_context_data()
        formset_insumos = context["insumos"]
        formset_imagenes = context["imagenes"]

        # Guardar producto
        self.object = form.save()

        if formset_insumos.is_valid() and formset_imagenes.is_valid():
            formset_insumos.instance = self.object
            formset_insumos.save()

            formset_imagenes.instance = self.object
            formset_imagenes.save()

            # Guardar producto completo
            return super().form_valid(form)

        # Repopular form con errores
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("productos:detail", kwargs={"pk": self.object.pk})


class ProductoDetailView(DetailView):
    model = Producto

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(*args, **kwargs)
        return context


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy("productos:list")
