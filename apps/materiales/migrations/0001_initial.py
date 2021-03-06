# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0002_auto_20180527_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('existencia', models.CharField(max_length=50, verbose_name='Existencia')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
