# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='precio',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
