from dal import autocomplete
from .models import Proveedor
from django.db.models import Q


class ProveedorAutocomplete(autocomplete.Select2QuerySetView):
    """
     Base de autompletado para proveedores.
    """

    def get_queryset(self):

        # Buscar proveedores
        qs = Proveedor.objects.all()

        # Filtrarlos si existe una búsqueda
        if self.q:
            qs = qs.filter(Q(razon_social__icontains=self.q))

        # Devolverlos ordenados por nombre
        return qs.order_by("razon_social")
