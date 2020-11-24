import factory


class ClienteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "clientes.Cliente"

    nombre = factory.Sequence(lambda n: "Nombre %03d" % n)
    apellido = factory.Sequence(lambda n: "Apellido %03d" % n)

    localidad = factory.SubFactory("core.tests.factories.LocalidadFactory")
