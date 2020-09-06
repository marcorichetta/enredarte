import factory


class UnidadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "productos.Unidad"

    nombre = factory.Sequence(lambda n: "Unidad %d" % n)


class InsumoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "productos.Insumo"

    nombre = factory.Sequence(lambda n: "Insumo %d" % n)  # Insumo N
    unidad_medida = factory.SubFactory(UnidadFactory)
    precio = factory.Sequence(lambda n: "%d00" % n)  # 100 - 200 - 300

    # ManyToMany Relation
    # https://factoryboy.readthedocs.io/en/latest/recipes.html#simple-many-to-many-relationship
    @factory.post_generation
    def proveedores(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing
            return

        if extracted:
            # Una lista de proveedores fueron pasados como arg, usálos
            for proveedor in extracted:
                self.proveedores.add(proveedor)


class ProductoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "productos.Producto"

    nombre = factory.Sequence(lambda n: "Producto %d" % n)  # Producto N
    tiempo = factory.Faker("pyint", min_value=0, max_value=360)

    insumo_base = factory.SubFactory(InsumoFactory)
    insumo_lados = factory.SubFactory(InsumoFactory)

    @factory.post_generation
    def insumos(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing
            return

        if extracted:
            # Una lista de insumos fueron pasados como arg, usálos
            for insumo in extracted:
                self.insumos.add(insumo)
