# !/usr/bin/python

from django.core.management.base import BaseCommand
import sys
from variables.models import Variable


class Command(BaseCommand):
    help = """Crea variables iniciales"""

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- Creando variables de prueba ---"))

        v = Variable()
        v.precio_hora = 40
        v.precio_pintado = 50
        v.ganancia_por_mayor = 45
        v.ganancia_por_menor = 55
        v.ganancia_fibrofacil = 15

        v.save()

        self.stdout.write(self.style.SUCCESS("--- Creación de variables finalizada ---"))
