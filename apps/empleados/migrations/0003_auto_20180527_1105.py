# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_auto_20180527_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puestos.Puesto'),
        ),
    ]
