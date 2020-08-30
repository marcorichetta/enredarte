import factory


class PedidoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "pedidos.Pedido"
