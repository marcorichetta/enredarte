# !/usr/bin/python

from django.core.management.base import BaseCommand
import sys
from utiles.factories import *


class Command(BaseCommand):
    help = """Crea insumos iniciales"""

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- Creando insumos de prueba ---"))

        InsumoFactory(nombre="MDF-3", precio=206, proveedores=1)
        InsumoFactory(nombre="MDF-5", precio=300, proveedores=1)
        InsumoFactory(nombre="Cola Vinilica", precio=90, proveedores=1)
