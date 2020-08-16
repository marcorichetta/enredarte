# !/usr/bin/python

from django.core.management.base import BaseCommand
import sys
from core.models import Provincia, Localidad


class Command(BaseCommand):
    help = """Crea las provincias y localidades iniciales"""

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("--- Creando provincias y localidades de prueba ---")
        )
        Provincia.objects.create(cod_provincia="AR-B", provincia="Buenos Aires")
        Provincia.objects.create(cod_provincia="AR-C", provincia="Capital Federal")
        Provincia.objects.create(cod_provincia="AR-K", provincia="Catamarca")
        Provincia.objects.create(cod_provincia="AR-H", provincia="Chaco")
        cba = Provincia.objects.create(cod_provincia="AR-X", provincia="Córdoba")
        Provincia.objects.create(cod_provincia="AR-W", provincia="Corrientes")
        Provincia.objects.create(cod_provincia="AR-E", provincia="Entre Ríos")
        Provincia.objects.create(cod_provincia="AR-P", provincia="Formosa")
        Provincia.objects.create(cod_provincia="AR-Y", provincia="Jujuy")
        Provincia.objects.create(cod_provincia="AR-L", provincia="La Pampa")
        Provincia.objects.create(cod_provincia="AR-F", provincia="La Rioja")
        Provincia.objects.create(cod_provincia="AR-M", provincia="Mendoza")
        Provincia.objects.create(cod_provincia="AR-N", provincia="Misiones")
        Provincia.objects.create(cod_provincia="AR-Q", provincia="Neuquén")
        Provincia.objects.create(cod_provincia="AR-R", provincia="Río Negro")
        Provincia.objects.create(cod_provincia="AR-A", provincia="Salta")
        Provincia.objects.create(cod_provincia="AR-J", provincia="San Juan")
        Provincia.objects.create(cod_provincia="AR-D", provincia="San Luis")
        Provincia.objects.create(cod_provincia="AR-Z", provincia="Santa Cruz")
        Provincia.objects.create(cod_provincia="AR-S", provincia="Santa Fe")
        Provincia.objects.create(cod_provincia="AR-G", provincia="Santiago del Estero")
        Provincia.objects.create(cod_provincia="AR-V", provincia="Tierra del Fuego")
        Provincia.objects.create(cod_provincia="AR-T", provincia="Tucumán")

        Localidad.objects.create(
            cod_postal=5000, localidad="Córdoba Capital", provincia=cba
        )
        Localidad.objects.create(cod_postal=5921, localidad="Las Perdices", provincia=cba)
        Localidad.objects.create(
            cod_postal=5923, localidad="General Deheza", provincia=cba
        )
        Localidad.objects.create(
            cod_postal=5809, localidad="General Cabrera", provincia=cba
        )
        Localidad.objects.create(cod_postal=5800, localidad="Río Cuarto", provincia=cba)
        Localidad.objects.create(cod_postal=5900, localidad="Villa María", provincia=cba)

        self.stdout.write(self.style.SUCCESS("--- Provincias y Localidades creadas ---"))
