from django.test import TestCase

# Unit tests para el modelo Cliente

from clientes.models import Cliente
from gestion.models import Localidad, Provincia
import datetime


class ClienteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        # Creamos la data necesaria para realizar los tests
        provTest = Provincia.objects.create(cod_provincia='TEST', provincia='CBA', )
        locTest = Localidad.objects.create(cod_postal=1, localidad='LP', provincia=provTest)

        Cliente.objects.create(
            nombre='Marco',
            apellido='Richetta',
            email='marcorichetta@gmail.com',
            telefono='3534123456',
            calle='Santa Fe',
            numero='565',
            localidad=locTest,
        )

    def test_creacion_correcta(self):
        cliente = Cliente.objects.get(id=1)

        self.assertTrue(isinstance(cliente, Cliente))

    def test_get_absolute_url(self):
        """ El método get_absolute_url debe dirigir a la página inicial de Clientes """

        cliente = Cliente.objects.get(id=1)

        self.assertEquals(Cliente.get_absolute_url(self), '/clientes/')
