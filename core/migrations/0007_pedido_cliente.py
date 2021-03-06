# Generated by Django 2.2.3 on 2019-07-18 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0001_squashed_0004_auto_20191101_1227"),
        ("core", "0001_squashed_0006_auto_20190718_1239"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedido",
            name="cliente",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="clientes.Cliente",
            ),
            preserve_default=False,
        )
    ]
