import json
from django.test import TestCase, Client

# Tests para views de Localidad y Provincia

from gestion.models import Localidad, Provincia


class LocalidadView(TestCase):

    @classmethod
    def setUpTestData(cls):

        # Creamos la data necesaria para realizar los tests
        Provincia.objects.create(cod_provincia='TEST', provincia='CBA')

    def test_ajax_request_nueva_localidad(self):
        """ Crea una nueva localidad simulando la request del modal de la página de Clientes"""

        testData = {
            'cod_postal': '9999',
            'localidad': 'Test',
            'provincia_id': '1'
        }

        # No definir el content-type de la request
        self.client.post('/localidad/new/', testData)

        localidadCreada = Localidad.objects.get(id=1)

        # Los valores esperados
        valoresEsperados = ['9999', 'Test', 1]

        valoresEnDB = [
            localidadCreada.cod_postal,
            localidadCreada.localidad,
            localidadCreada.provincia_id
        ]

        self.assertListEqual(valoresEnDB, valoresEsperados)
