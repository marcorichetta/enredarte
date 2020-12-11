# !/usr/bin/python

from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    help = """Crea las provincias y localidades iniciales"""

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("--- Creando superusuario y usuario de prueba ---")
        )

        CustomUser.objects.create_superuser(username="root", password="root", email=None)
        CustomUser.objects.create_user(username="gerencia", password="gerencia")
        CustomUser.objects.create_user(username="operario", password="operario")

        self.stdout.write(self.style.SUCCESS("--- Usuarios creados ---"))
