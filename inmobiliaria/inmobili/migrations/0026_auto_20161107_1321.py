# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-07 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmobili', '0025_auto_20161107_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='casa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inmobili.Casa'),
        ),
    ]