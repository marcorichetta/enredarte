# Generated by Django 2.2.3 on 2019-11-01 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20190806_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clientes', to='gestion.Localidad'),
        ),
    ]