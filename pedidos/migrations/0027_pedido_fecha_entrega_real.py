# Generated by Django 2.2.13 on 2020-12-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pedidos", "0026_auto_20201126_1736"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedido",
            name="fecha_entrega_real",
            field=models.DateField(
                blank=True, null=True, verbose_name="Fecha de entrega real"
            ),
        ),
    ]
