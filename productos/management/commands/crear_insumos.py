# !/usr/bin/python

from django.core.management.base import BaseCommand
from productos.models import Unidad, Insumo
from proveedores.models import Proveedor

class Command(BaseCommand):
    help = """Crea insumos iniciales"""

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- Creando unidades de prueba ---"))

        p1 = Proveedor.objects.get(id=1)
        p2 = Proveedor.objects.get(id=2)


        mm = Unidad.objects.get_or_create(
            nombre="mm",
            descripcion="Milímetro"
        )

        kg = Unidad.objects.get_or_create(
            nombre="kg",
            descripcion="Kilogramo"
        )

        unitario = Unidad.objects.get_or_create(
            nombre="U",
            descripcion="Unidad"
        )

        self.stdout.write(self.style.SUCCESS("--- Creando insumos de prueba ---"))
        
        i1 = Insumo.objects.create(
            nombre='MDF-3',
            descripcion='Fibrofacil de 3mm',
            medida='3',
            unidad_medida=mm[0],
            precio='206',
        )

        i2 = Insumo.objects.create(
            nombre='MDF-5',
            descripcion='Fibrofacil de 5mm',
            medida='5',
            unidad_medida=mm[0],
            precio='300',
        )

        i3 = Insumo.objects.create(
            nombre='Cola vinílica',
            descripcion='Cola vinílica',
            medida='1',
            unidad_medida=kg[0],
            precio='90',
        )

        i4 = Insumo.objects.create(
            nombre='Insumo extra',
            descripcion='Insumo de prueba',
            medida='1',
            unidad_medida=unitario[0],
            precio='100',
        )

        self.stdout.write(self.style.SUCCESS("--- Relaciones de insumos con proveedores ---"))

        i1.proveedores.set([p1])
        i2.proveedores.set([p1])
        i3.proveedores.set([p1, p2])
        i4.proveedores.set([p2, p1])

        self.stdout.write(self.style.SUCCESS("--- Unidades e Insumos creados ---"))
