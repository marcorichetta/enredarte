import factory


class ProveedorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "proveedores.Proveedor"

    localidad = factory.SubFactory("core.tests.factories.LocalidadFactory")
