import pytest

from clientes.forms import ClienteForm
from .factories import ClienteFactory
from core.tests.factories import LocalidadFactory
from clientes.models import Cliente


@pytest.fixture
def form_cliente() -> ClienteForm:
    """ Set up de un formulario de cliente """

    ClienteFactory(nombre="Cliente", apellido="1", cuit="30-52999943-3")

    form = ClienteForm({"nombre": "Cliente", "apellido": "2", "cuit": "30-52999943-3",})

    return form


@pytest.mark.django_db()
def test_form_cliente_cuit_duplicado_muestra_error(form_cliente):
    """ Si se crea un cliente mediante el formulario con un cuit ya existente se devuelve error """

    assert not form_cliente.is_valid()

    errores = form_cliente.errors
    error_cuit = errores.get("cuit")[0]

    assert error_cuit == "Ya existe un/a Cliente con este/a Cuit."


@pytest.mark.django_db()
def test_form_cliente_cuit_duplicado_muestra_error_SOFT_DELETE(form_cliente):
    """
        Si se crea un cliente mediante el formulario con un cuit ya existente
        (Borrado lógicamente) se devuelve error
    """

    # Soft delete
    prov1 = Cliente.objects.get(cuit="30-52999943-3")
    prov1.delete()

    # Aunque esté borrado lógicamente no se puede crear un cliente
    # con el mismo cuit porque todavía existe en la DB

    assert not form_cliente.is_valid()

    errores = form_cliente.errors.as_data()
    error_cuit = errores.get("cuit")[0]

    assert error_cuit.code == "cuit duplicado"


def forms_cuit_en_blanco():

    # El pk de la localidad está hardcoded. Se crea en el siguiente test.
    return [
        {"cuit": "", "nombre": "Usuario", "apellido": "1", "localidad": 1,},
        {"cuit": "   ", "nombre": "Usuario", "apellido": "2", "localidad": 1,},
    ]


@pytest.mark.django_db()
@pytest.mark.parametrize("form_data", forms_cuit_en_blanco())
def test_form_con_cuit_en_blanco(form_data):
    """
        Si se crea un cliente con el cuit vacío se guarda con None.

        https://docs.djangoproject.com/en/3.1/ref/models/fields/#null
        https://stackoverflow.com/a/15534514/6389248
    """

    LocalidadFactory()

    form = ClienteForm(data=form_data)

    print(form.errors)
    assert form.is_valid()
    assert form.cleaned_data["cuit"] is None
    assert form.instance.cuit is None
