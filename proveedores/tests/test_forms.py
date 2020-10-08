import pytest

from proveedores.forms import ProveedorForm
from .factories import ProveedorFactory
from core.tests.factories import LocalidadFactory
from proveedores.models import Proveedor


@pytest.fixture
def form_proveedor() -> ProveedorForm:
    """ Set up de un formulario de proveedor """

    ProveedorFactory(cuit="30-52999943-3", razon_social="Prueba")

    loc1 = LocalidadFactory()

    form = ProveedorForm(
        {"cuit": "30-52999943-3", "razon_social": "Prueba 2", "localidad": loc1.pk,}
    )

    return form


@pytest.mark.django_db()
def test_form_proveedor_cuit_duplicado_muestra_error(form_proveedor):
    """ Si se crea un proveedor mediante el formulario con un cuit ya existente se devuelve error """

    assert not form_proveedor.is_valid()

    errores = form_proveedor.errors
    error_cuit = errores.get("cuit")[0]

    assert error_cuit == "Ya existe un/a Proveedor con este/a Cuit."


@pytest.mark.django_db()
def test_form_proveedor_cuit_duplicado_muestra_error_SOFT_DELETE(form_proveedor):
    """ Si se crea un proveedor mediante el formulario con un cuit ya existente (Borrado lógicamente) se devuelve error """

    # Soft delete
    prov1 = Proveedor.objects.get(cuit="30-52999943-3")
    prov1.delete()

    # Aunque esté borrado lógicamente no se puede crear un proveedor con el mismo cuit porque todavía existe en la DB

    assert not form_proveedor.is_valid()

    errores = form_proveedor.errors.as_data()
    error_cuit = errores.get("cuit")[0]

    assert error_cuit.code == "cuit duplicado"
