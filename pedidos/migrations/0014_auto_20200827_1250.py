# Generated by Django 2.2.10 on 2020-08-27 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pedidos", "0013_auto_20200816_0621"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pedido", old_name="precio_final", new_name="precio_total",
        ),
    ]