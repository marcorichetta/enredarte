import pytest
from django.test import TestCase

from productos.forms import InsumosProductoFormset, ProductoForm
from productos.models import Insumo, Producto, Unidad
from productos.tests.factories import InsumoFactory, UnidadFactory
from variables.models import Variable
from variables.tests.factories import VariableFactory

# Unit tests para el form de creación de Producto


@pytest.fixture
def form_producto() -> ProductoForm:
    """ Set up de un formulario de producto """

    insumo1 = InsumoFactory(nombre="MDF-3", precio=100)  # MDF-3

    insumo2 = InsumoFactory(nombre="MDF-5", precio=200)  # MDF-5

    form = ProductoForm(
        {
            "nombre": "MDF-Prueba",
            "descripcion": "Prueba",
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

    assert form_producto.is_valid()
    assert form_producto.cleaned_data["insumo_base"].nombre == "MDF-3"
    assert form_producto.cleaned_data["insumo_lados"].nombre == "MDF-5"


@pytest.mark.django_db
def test_calculo_precio_producto(form_producto):
    """ Se calcula el precio de un producto en base a sus 
        insumos y a las variables globales del sistema
    """

    Variable.objects.create(
        precio_hora=40,
        precio_pintado=50,
        ganancia_por_mayor=45,
        ganancia_por_menor=55,
        ganancia_fibrofacil=15,
    )

    prod1: Producto = form_producto.save()

    assert prod1.precio_costo() == 40
    assert prod1.precio_venta_crudo == 62
    assert prod1.precio_terminado == 176
    assert prod1.precio_venta_terminado == 273
