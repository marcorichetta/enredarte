# Generated by Django 2.2.10 on 2020-09-28 22:14

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("compras", "0007_auto_20200907_0005"),
    ]

    operations = [
        migrations.AlterField(
            model_name="insumoscompra",
            name="cantidad",
            field=models.DecimalField(
                decimal_places=1,
                default=0,
                max_digits=4,
                validators=[django.core.validators.MinValueValidator(Decimal("0.0"))],
            ),
        ),
    ]
