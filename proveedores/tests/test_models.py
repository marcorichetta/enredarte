import pytest
from proveedores.models import Proveedor
from .factories import ProveedorFactory
from django.db import IntegrityError


@pytest.mark.django_db()
def test_soft_delete_no_deja_crear_en_BD_unique_key():
    """ Crear proveedor con mismo CUIT que un registro existente da error de integridad """

    proveedor = ProveedorFactory(cuit="30-52999943-3", razon_social="Prueba")

    assert Proveedor.all_objects.count() == 1

    proveedor.delete()

    # El manager `objects` devuelve sólo las instancias activas
    assert Proveedor.objects.count() == 0
    # El manager `all_objects` devuelve todas las instancias creadas
    assert Proveedor.all_objects.count() == 1

    # Nuevo proveedor con mismo cuit (Unique key) da error de integridad
    with pytest.raises(IntegrityError):
        ProveedorFactory(cuit="30-52999943-3", razon_social="Prueba")


@pytest.mark.django_db()
def test_proveedor_se_puede_restaurar():
    """ Proveedor borrado lógicamente se puede restaurar """

    prov = ProveedorFactory(cuit="30-52999943-3", razon_social="Prueba")

    prov.delete()

    assert prov.is_removed == True
    assert Proveedor.objects.count() == 0
    assert Proveedor.all_objects.count() == 1

    prov.is_removed = False
    prov.save()

    assert Proveedor.objects.count() == 1
