import pytest
from proveedores.models import Proveedor
from .factories import ProveedorFactory


@pytest.mark.django_db()
@pytest.mark.skip(reason="No tiene sentido ahora")
def test_soft_delete_no_deja_crear_en_BD_unique_key():

    proveedor = ProveedorFactory(cuit=305299994393, razon_social="Prueba")

    assert Proveedor.all_objects.count() == 1

    proveedor.delete()

    # El manager `objects` devuelve sólo las instancias activas
    assert Proveedor.objects.count() == 0
    # El manager `all_objects` devuelve todas las instancias creadas
    assert Proveedor.all_objects.count() == 1

    # Crear nuevo proveedor con mismo cuit (Unique key)
    proveedor2 = ProveedorFactory(cuit=305299994393, razon_social="Prueba")
