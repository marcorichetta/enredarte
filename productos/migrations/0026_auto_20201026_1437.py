# Generated by Django 2.2.10 on 2020-10-26 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0025_auto_20201020_0112"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="regular",
            options={
                "verbose_name": "Producto Regular",
                "verbose_name_plural": "Productos Regulares",
            },
        ),
    ]