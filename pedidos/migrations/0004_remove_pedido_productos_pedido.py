# Generated by Django 2.2.3 on 2019-08-01 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_productospedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='productos_pedido',
        ),
    ]