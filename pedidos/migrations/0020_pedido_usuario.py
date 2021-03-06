# Generated by Django 2.2.13 on 2020-11-05 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pedidos", "0019_auto_20201102_1919"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedido",
            name="usuario",
            field=models.ForeignKey(
                help_text="Usuario que registra el pedido",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
