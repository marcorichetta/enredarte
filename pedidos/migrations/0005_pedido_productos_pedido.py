# Generated by Django 2.2.3 on 2019-08-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_remove_producto_slug'),
        ('pedidos', '0004_remove_pedido_productos_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='productos_pedido',
            field=models.ManyToManyField(through='pedidos.ProductosPedido', to='productos.Producto'),
        ),
    ]
