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
