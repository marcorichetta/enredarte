# Generated by Django 2.2.3 on 2019-07-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_auto_20190705_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localidad',
            name='cod_postal',
            field=models.CharField(max_length=10),
        ),
    ]