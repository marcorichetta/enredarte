# Generated by Django 2.2.10 on 2020-10-09 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0022_auto_20200928_1826"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="insumosproducto",
            options={
                "verbose_name": "Insumo del Producto",
                "verbose_name_plural": "Insumos del Producto",
            },
        ),
        migrations.AlterModelOptions(
            name="productimage",
            options={
                "verbose_name": "Imagen de Producto",
                "verbose_name_plural": "Imágenes del Producto",
            },
        ),
    ]
