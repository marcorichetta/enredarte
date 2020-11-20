from django.views.generic import DetailView
from pedidos.models import OrdenTrabajo


class OrdenTrabajoDetailView(DetailView):
    model = OrdenTrabajo
    template_name = "pedidos/orden_trabajo_detail.html"

    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     modified_qs = OrdenTrabajo.objects \
    #         .select_related("pedido") \
    #         .prefetch_related("pedido__productos_pedido") \

    #     return modified_qs
