# !/usr/bin/python

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    help = """Crea los grupos y permisos para ser asignados a los usuarios"""

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- Creando grupos ---"))

        """ Asignar los permisos iniciales a los roles en el sistema """
        grupo_operario, created = Group.objects.get_or_create(name="grupo_operario")
        permiso_ver_OT = Permission.objects.get(
            codename="view_ordentrabajo", content_type__app_label="pedidos"
        )
        grupo_operario.permissions.add(permiso_ver_OT)

        grupo_administrativo, created = Group.objects.get_or_create(
            name="grupo_administrativo"
        )

        permiso_ver_pedidos = Permission.objects.get(
            codename="view_pedido", content_type__app_label="pedidos"
        )

        permiso_ver_clientes = Permission.objects.get(
            codename="view_cliente", content_type__app_label="clientes"
        )

        permiso_ver_productos = Permission.objects.get(
            codename="view_producto", content_type__app_label="productos"
        )
        permiso_modificar_precio = Permission.objects.get(
            codename="change_product_price", content_type__app_label="productos"
        )
        permiso_modificar_descuento = Permission.objects.get(
            codename="change_discount", content_type__app_label="pedidos"
        )
        grupo_administrativo.permissions.add(
            permiso_modificar_precio,
            permiso_modificar_descuento,
            permiso_ver_pedidos,
            permiso_ver_clientes,
            permiso_ver_productos,
        )

        self.stdout.write(
            self.style.SUCCESS("--- Grupos creados y permisos asignados ---")
        )

        self.stdout.write("================================================")

        self.stdout.write(
            self.style.SUCCESS("--- Creando superusuario y usuario de prueba ---")
        )

        CustomUser.objects.create_superuser(username="root", password="root", email=None)
        admin = CustomUser.objects.create_user(
            username="administrativo", password="administrativo"
        )
        operario = CustomUser.objects.create_user(
            username="operario", password="operario"
        )

        admin.groups.add(grupo_administrativo)
        operario.groups.add(grupo_operario)

        self.stdout.write(
            self.style.SUCCESS("--- Usuarios creados y asignados a sus grupos---")
        )
