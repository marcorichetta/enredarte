import factory

from productos import models
from proveedores.models import Proveedor
from gestion.models import Localidad, Provincia


class UnidadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Unidad

    nombre = factory.Sequence(lambda n: "Unidad %d" % n)


class ProvinciaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Provincia


class LocalidadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Localidad

    localidad = factory.Sequence(lambda n: "Localidad %d" % n)
    provincia = factory.SubFactory(ProvinciaFactory)


class ProveedorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Proveedor

    localidad = factory.SubFactory(LocalidadFactory)


class InsumoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Insumo

    nombre = "MDF-3"
    unidad_medida = factory.SubFactory(UnidadFactory)
    precio = factory.Sequence(lambda n: "%d00" % n)  # 100 - 200 - 300

    # ManyToMany Rel
    @factory.post_generation
    def proveedores(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing
            return

        if extracted:
            # Una lista de proveedores fueron pasados como arg, usálos
            for proveedor in extracted:
                self.proveedores.add(proveedor)
