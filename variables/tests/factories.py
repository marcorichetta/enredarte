import factory
from factory.fuzzy import FuzzyDecimal


class VariableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "variables.Variable"

    precio_hora = FuzzyDecimal(
        0.0, 99.9, 2
    )  # Número entre 0 y 100 con precisión de 2 decimales
    precio_pintado = FuzzyDecimal(0.0, 99.9, 2)
    ganancia_por_mayor = FuzzyDecimal(0.0, 99.9, 2)
    ganancia_por_menor = FuzzyDecimal(0.0, 99.9, 2)
    ganancia_fibrofacil = FuzzyDecimal(0.0, 99.9, 2)
