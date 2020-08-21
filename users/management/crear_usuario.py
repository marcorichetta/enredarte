# !/usr/bin/python

from django.core.management.base import BaseCommand
import sys
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = """Crea las provincias y localidades iniciales"""

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("--- Creando superusuario y usuario de prueba ---")
        )

        User.objects.create_superuser(username="root", password="root", email=None)
        User.objects.create_user(username="test", password="test")

        self.stdout.write(self.style.SUCCESS("--- Usuarios creados ---"))
