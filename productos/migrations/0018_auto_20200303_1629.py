# Generated by Django 2.2.3 on 2020-03-03 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0017_auto_20191128_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='productos.Producto'),
        ),
    ]
