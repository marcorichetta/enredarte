# Generated by Django 2.2.10 on 2020-04-02 22:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    # replaces = [('clientes', '0001_initial'), ('clientes', '0002_auto_20190722_1526'), ('clientes', '0003_auto_20190806_1806'), ('clientes', '0004_auto_20191101_1227')]

    initial = True

    dependencies = [("core", "0001_squashed_0006_auto_20190718_1239")]

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=64)),
                ("apellido", models.CharField(max_length=64)),
                ("email", models.EmailField(max_length=254)),
                ("telefono", models.CharField(max_length=64)),
                ("calle", models.CharField(max_length=64)),
                ("numero", models.CharField(max_length=6)),
                ("detalles", models.TextField(blank=True)),
                (
                    "localidad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clientes",
                        to="core.Localidad",
                    ),
                ),
            ],
            options={"db_table": "clientes_cliente", "ordering": ["nombre", "apellido"]},
        ),
        migrations.AlterModelTable(name="cliente", table=None),
        migrations.AddField(
            model_name="cliente",
            name="fecha_creacion",
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cliente",
            name="calle",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="numero",
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="telefono",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="localidad",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="clientes",
                to="core.Localidad",
            ),
        ),
    ]
