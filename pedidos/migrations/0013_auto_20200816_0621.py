# Generated by Django 2.2.10 on 2020-08-16 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("pedidos", "0012_auto_20200816_0617")]

    operations = [
        migrations.AlterField(
            model_name="productospedido",
            name="producto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="productos.Producto"
            ),
        )
    ]
