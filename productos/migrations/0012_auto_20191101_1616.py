# Generated by Django 2.2.3 on 2019-11-01 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_auto_20190809_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='unidad_medida',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='unidades', to='productos.Unidad'),
        ),
    ]
