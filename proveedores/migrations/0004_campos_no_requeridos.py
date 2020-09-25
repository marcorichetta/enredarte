# Generated by Django 2.2.10 on 2020-09-21 01:36

from django.db import migrations, models
import proveedores.helpers


class Migration(migrations.Migration):

    dependencies = [
        ("proveedores", "0003_agg_base_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proveedor",
            name="calle",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="cuit",
            field=models.CharField(
                blank=True,
                help_text="Ingrese el CUIT con el siguiente formato: 20-12345678-9",
                max_length=13,
                unique=True,
                validators=[proveedores.helpers.validar_cuit],
            ),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="numero",
            field=models.CharField(blank=True, max_length=4),
        ),
    ]