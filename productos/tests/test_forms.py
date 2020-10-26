import pytest

from productos.forms import ProductoRegularForm
from productos.models import Producto
from productos.tests.factories import InsumoFactory
from variables.models import Variable

# Unit tests para el form de creación de Producto


@pytest.fixture
def form_producto() -> ProductoRegularForm:
    """ Set up de un formulario de producto """

    insumo1 = InsumoFactory(nombre="MDF-3", precio=100)  # MDF-3

    insumo2 = InsumoFactory(nombre="MDF-5", precio=200)  # MDF-5

    form = ProductoRegularForm(
        {
            "nombre": "MDF-Prueba",
            "descripcion": "Prueba",
            "tipo": "regular",
            "largo": "20",
            "ancho": "15",
            "alto": "4",
            "tiempo": "50",
            "insumo_base": insumo1.pk,
            "insumo_lados": insumo2.pk,
        }
    )

    return form


@pytest.mark.django_db
def test_insumos_correctos(django_db_setup, form_producto):
    """ Insumo base y lados deben mostrar solamente opciones de Fibrofacil """

    print(form_producto.errors)
    assert form_producto.is_valid()
    assert form_producto.cleaned_data["insumo_base"].nombre == "MDF-3"
    assert form_producto.cleaned_data["insumo_lados"].nombre == "MDF-5"


@pytest.mark.django_db
def test_calculo_precio_producto(form_producto):
    """ Se calcula el precio de un producto en base a sus
        insumos y a las variables globales del sistema
    """

    variables = Variable.objects.create(
        precio_hora=40,
        precio_pintado=50,
        ganancia_por_mayor=45,
        ganancia_por_menor=55,
        ganancia_fibrofacil=15,
    )

    prod1: Producto = form_producto.save()

    assert round(prod1.precio_costo(variables)) == 42
    assert round(prod1.precio_venta_crudo()) == 64
    assert round(prod1.precio_terminado(variables)) == 158
    assert round(prod1.precio_venta_terminado()) == 245
