import factory
from factory import fuzzy
from pedidos.models import Pedido
import datetime


class PedidoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "pedidos.Pedido"

    cliente = factory.SubFactory("clientes.tests.factories.ClienteFactory")

    estado = fuzzy.FuzzyChoice(
        choices=Pedido.ESTADO_PEDIDO_CHOICES, getter=lambda c: c[0]
    )
    precio_total = fuzzy.FuzzyDecimal(low=100, high=5000)
    fecha_entrega = fuzzy.FuzzyDate(start_date=datetime.date(2020, 9, 1))

    @factory.post_generation
    def productos_pedido(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing
            return

        if extracted:
            # Una lista de productos fueron pasados como arg, usálos
            for producto in extracted:
                self.productos_pedido.add(producto)
