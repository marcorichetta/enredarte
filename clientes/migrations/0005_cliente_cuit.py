# Generated by Django 2.2.10 on 2020-10-10 22:49

from django.db import migrations, models
import proveedores.helpers


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0004_auto_20200816_0513"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="cuit",
            field=models.CharField(
                blank=True,
                help_text="Ingrese el CUIT con el siguiente formato: 20-12345678-9",
                max_length=13,
                null=True,
                unique=True,
                validators=[proveedores.helpers.validar_cuit],
            ),
        ),
    ]
