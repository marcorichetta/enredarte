# Generated by Django 2.2.3 on 2019-08-27 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0011_auto_20190809_1743'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalles', models.TextField(blank=True)),
                ('fecha_compra', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-fecha_compra'],
            },
        ),
        migrations.CreateModel(
            name='InsumosCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Compra')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Insumo')),
            ],
            options={
                'verbose_name_plural': 'InsumosCompras',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='insumos_compra',
            field=models.ManyToManyField(through='compras.InsumosCompra', to='productos.Insumo'),
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor'),
        ),
    ]