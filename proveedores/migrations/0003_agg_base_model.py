# Generated by Django 2.2.10 on 2020-08-16 07:32

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("proveedores", "0002_auto_20191101_1227"),
    ]

    operations = [
        migrations.AddField(
            model_name="proveedor",
            name="created",
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now, editable=False, verbose_name="created"
            ),
        ),
        migrations.AddField(
            model_name="proveedor",
            name="is_removed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="proveedor",
            name="modified",
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now, editable=False, verbose_name="modified"
            ),
        ),
    ]
