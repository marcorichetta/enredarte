# !/usr/bin/python

from django.core.management.base import BaseCommand
import sys
from gestion.models import Localidad
from proveedores.models import Proveedor


class Command(BaseCommand):
    help = """Crea proveedores iniciales"""

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- Creando proveedores de prueba ---"))
        villamaria = Localidad.objects.get(cod_postal=5900)
        rio4 = Localidad.objects.get(cod_postal=5800)
        cba = Localidad.objects.get(cod_postal=5000)

        Proveedor.objects.create(
            cuit="30-4219859-3",
            razon_social="ALEMANN S.R.L.",
            telefono="123456789",
            email="empresa@proveedor.com",
            calle="Sarmiento",
            numero="789",
            localidad=villamaria,
        )
        Proveedor.objects.create(
            cuit="30-59895662-2",
            razon_social="VIA PUBLICA CLAN S.A.",
            telefono="123456789",
            email="empresa@proveedor.com",
            calle="Sarmiento",
            numero="789",
            localidad=cba,
        )

        Proveedor.objects.create(
            cuit="30-50259063-0",
            razon_social="ATACAMA SA DE PUBLICIDAD",
            telefono="123456789",
            email="empresa@proveedor.com",
            calle="Sarmiento",
            numero="789",
            localidad=rio4,
        )

        Proveedor.objects.create(
            cuit="30-64391342-5",
            razon_social="Red Celeste y Blanca S.A.",
            telefono="123456789",
            email="empresa@proveedor.com",
            calle="San Juan",
            numero="789",
            localidad=cba,
        )

        Proveedor.objects.create(
            cuit="30-68296025-2",
            razon_social="e.a. carnevale y cia s.a.",
            telefono="123456789",
            email="empresa@proveedor.com",
            calle="Belgrano",
            numero="123",
            localidad=villamaria,
        )

        self.stdout.write(self.style.SUCCESS("--- Proveedores creados ---"))
