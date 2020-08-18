import pytest

# Unit tests para el form de creación de Producto

from productos.models import Insumo, Producto, Unidad
from productos.forms import InsumosProductoFormset, ProductoForm
from .factories import InsumoFactory, UnidadFactory


@pytest.fixture
def form_producto():
    """ Set up de un formulario de producto """

    insumo1 = InsumoFactory()  # MDF-3

    insumo2 = InsumoFactory(nombre="MDF-5")  # MDF-5

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
