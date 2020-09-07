# Generated by Django 2.2.10 on 2020-09-07 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("variables", "0002_agg_base_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variable",
            name="ganancia_fibrofacil",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Porcentaje de ganancia aplicada al fibrofacil",
                max_digits=5,
            ),
        ),
        migrations.AlterField(
            model_name="variable",
            name="ganancia_por_mayor",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Porcentaje de ganancia por mayor",
                max_digits=5,
            ),
        ),
        migrations.AlterField(
            model_name="variable",
            name="ganancia_por_menor",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Porcentaje de ganancia por menor",
                max_digits=5,
            ),
        ),
        migrations.AlterField(
            model_name="variable",
            name="precio_hora",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Precio de la hora de trabajo",
                max_digits=5,
            ),
        ),
        migrations.AlterField(
            model_name="variable",
            name="precio_pintado",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Precio de la pintura/apliques incluídos en el producto",
                max_digits=5,
            ),
        ),
    ]
