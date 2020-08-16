import factory


class ProvinciaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "core.Provincia"

    cod_provincia = factory.Sequence(lambda n: "AR-%d" % n)


class LocalidadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "core.Localidad"

    localidad = factory.Sequence(lambda n: "Localidad %d" % n)
    provincia = factory.SubFactory("core.tests.factories.ProvinciaFactory")
