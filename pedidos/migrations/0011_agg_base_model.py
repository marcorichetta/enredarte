# Generated by Django 2.2.10 on 2020-08-16 08:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("pedidos", "0010_auto_20200713_1650"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pedido", options={"ordering": ["-fecha_entrega", "-modified"]},
        ),
        migrations.RemoveField(model_name="pedido", name="actualizado",),
        migrations.RemoveField(model_name="pedido", name="fecha_pedido",),
        migrations.AddField(
            model_name="pedido",
            name="created",
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now, editable=False, verbose_name="created"
            ),
        ),
        migrations.AddField(
            model_name="pedido",
            name="is_removed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="pedido",
            name="modified",
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now, editable=False, verbose_name="modified"
            ),
        ),
        migrations.AddField(
            model_name="productospedido",
            name="created",
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now, editable=False, verbose_name="created"
            ),
        ),
        migrations.AddField(
            model_name="productospedido",
            name="is_removed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="productospedido",
            name="modified",
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now, editable=False, verbose_name="modified"
            ),
        ),
        migrations.AlterField(
            model_name="productospedido",
            name="pedido",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pedidos",
                to="pedidos.Pedido",
            ),
        ),
        migrations.AlterField(
            model_name="productospedido",
            name="producto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="productos",
                to="productos.Producto",
            ),
        ),
    ]
