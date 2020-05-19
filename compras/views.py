from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.db import transaction
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .models import Compra, InsumosCompra
from .forms import CompraForm, InsumosCompraFormset


class CompraListView(ListView):
    model = Compra
    template_name = "compras/compras.html"
    context_object_name = "compras"
    ordering = ["id"]
    paginate_by = 10

    def get_queryset(self):
        queryset = super(CompraListView, self).get_queryset()

        # Permite buscar en un form dentro de la misma página
        # con el formato q?<nombre-del-producto>
        query = self.request.GET.get("search")
        if query:
            return queryset.filter(Q(proveedor__razon_social__icontains=query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CompraListView, self).get_context_data(**kwargs)
        context["search_txt"] = self.request.GET.get("search", "")
        return context


class CompraCreateView(CreateView):
    model = Compra
    form_class = CompraForm

    def get_context_data(self, **kwargs):
        context = super(CompraCreateView, self).get_context_data(**kwargs)
        # Le agregamos los insumos al context para usarlos en el template
        if self.request.POST:
            context["insumos"] = InsumosCompraFormset(self.request.POST)
        else:
            context["insumos"] = InsumosCompraFormset()
        return context

    def form_valid(self, form):
        # Obtener info de compra e insumos posteados en el form
        context = self.get_context_data()
        insumos = context["insumos"]

        # Esto se ejecuta sólo si la transacción es atómica
        # https://docs.djangoproject.com/en/2.1/topics/db/transactions/#controlling-transactions-explicitly
        with transaction.atomic():
            # Guardar la compra
            self.object = form.save()
            # Si son válidos los insumos se guardan
            if insumos.is_valid():
                insumos.instance = self.object
                insumos.save()

                # Guardar compra completa
                return super(CompraCreateView, self).form_valid(form)

            # Repopular form con errores
            return self.render_to_response(self.get_context_data(form=form))


class CompraUpdateView(UpdateView):
    model = Compra
    form_class = CompraForm
    # Modify the template used for this view
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super(CompraUpdateView, self).get_context_data(**kwargs)

        # Enviar el objeto como instancia para ser actualizado
        if self.request.POST:
            context["insumos"] = InsumosCompraFormset(self.request.POST, instance=self.object)
        else:
            context["insumos"] = InsumosCompraFormset(instance=self.object)
        return context

    def form_valid(self, form):
        # Obtenemos info de la compra e insumos posteados en el form
        context = self.get_context_data()
        insumos = context["insumos"]

        # Esto se ejecuta sólo si la transacción es atómica
        # https://docs.djangoproject.com/en/2.1/topics/db/transactions/#controlling-transactions-explicitly
        with transaction.atomic():
            self.object = form.save()
            if insumos.is_valid():
                insumos.instance = self.object
                insumos.save()
                # Guardar compra completo
                return super(CompraUpdateView, self).form_valid(form)
            else:
                # Repopular form con errores
                return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("detailCompra", kwargs={"pk": self.object.pk})


class CompraDetailView(DetailView):
    model = Compra

    def get_context_data(self, *args, **kwargs):
        context = super(CompraDetailView, self).get_context_data(*args, **kwargs)
        return context


class CompraDeleteView(DeleteView):
    model = Compra
    success_url = reverse_lazy("compra")
