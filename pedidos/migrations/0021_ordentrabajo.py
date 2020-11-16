# Generated by Django 2.2.13 on 2020-11-16 15:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0005_cliente_cuit"),
        ("pedidos", "0020_pedido_usuario"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrdenTrabajo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("is_removed", models.BooleanField(default=False)),
                (
                    "estado",
                    models.IntegerField(
                        choices=[(0, "Creada"), (1, "En proceso"), (2, "Finalizado")],
                        default=0,
                    ),
                ),
                ("detalles", models.TextField(blank=True)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ordenes_de_trabajo",
                        to="clientes.Cliente",
                    ),
                ),
                (
                    "pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ordenes_de_trabajo",
                        to="pedidos.Pedido",
                    ),
                ),
            ],
            options={
                "verbose_name": "Orden de Trabajo",
                "verbose_name_plural": "Órdenes de Trabajo",
            },
        ),
    ]