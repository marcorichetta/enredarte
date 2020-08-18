import factory


class UnidadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "productos.Unidad"

    nombre = factory.Sequence(lambda n: "Unidad %d" % n)


class InsumoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "productos.Insumo"

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
