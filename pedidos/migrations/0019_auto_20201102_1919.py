# Generated by Django 2.2.13 on 2020-11-02 22:19

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pedidos", "0018_pedido_descuento"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pedido",
            options={
                "ordering": ["-fecha_entrega", "-modified"],
                "permissions": [("change_discount", "Can modify a Pedido discount")],
            },
        ),
        migrations.AlterField(
            model_name="pedido",
            name="descuento",
            field=models.DecimalField(
                decimal_places=0,
                default=0,
                help_text="% de descuento.",
                max_digits=2,
                validators=[django.core.validators.MinValueValidator(Decimal("0.0"))],
            ),
        ),
    ]