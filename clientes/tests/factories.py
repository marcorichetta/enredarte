import factory


class ClienteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "clientes.Cliente"

    localidad = factory.SubFactory("core.tests.factories.LocalidadFactory")
