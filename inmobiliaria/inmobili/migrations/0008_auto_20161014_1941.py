# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-14 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmobili', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='casa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inmobili.Casa'),
        ),
    ]
