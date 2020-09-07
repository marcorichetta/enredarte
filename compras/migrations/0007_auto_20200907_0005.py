# Generated by Django 2.2.10 on 2020-09-07 03:05

import datetime
from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("compras", "0006_auto_20200906_2205"),
    ]

    operations = [
        migrations.AlterField(
            model_name="compra",
            name="fecha_compra",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Fecha de compra"
            ),
        ),
        migrations.AlterField(
            model_name="insumoscompra",
            name="precio_compra",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Precio unitario",
                max_digits=6,
                validators=[django.core.validators.MinValueValidator(Decimal("0.0"))],
            ),
        ),
    ]
