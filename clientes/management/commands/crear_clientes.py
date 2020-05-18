# !/usr/bin/python

from django.core.management.base import BaseCommand
import sys
from gestion.models import Localidad
from clientes.models import Cliente


class Command(BaseCommand):
    help = """Crea clientes iniciales"""

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- Creando clientes de prueba ---"))
        perdices = Localidad.objects.get(cod_postal=5921)
        deheza = Localidad.objects.get(cod_postal=5923)

        Cliente.objects.create(
            nombre="Juan",
            apellido="Perez",
            email="jperez@hotmail.com",
            telefono="3534987654",
            calle="San Juan",
            numero="123",
            localidad=perdices,
        )
        Cliente.objects.create(
            nombre="Maria",
            apellido="Sanchez",
            email="msanchez@hotmail.com",
            telefono="3534987654",
            calle="Santa Rosa",
            numero="332",
            localidad=perdices,
        )
        Cliente.objects.create(
            nombre="Ricardo",
            apellido="Garcia",
            email="rgarcia@gmail.com",
            telefono="3534232342",
            calle="Alberdi",
            numero="754",
            localidad=deheza,
        )

        self.stdout.write(self.style.SUCCESS("--- Clientes creados ---"))
