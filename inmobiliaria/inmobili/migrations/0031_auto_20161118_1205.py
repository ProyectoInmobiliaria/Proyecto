# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-18 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmobili', '0030_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta',
            name='casa',
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='comment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='inmobili.Comment'),
        ),
    ]
