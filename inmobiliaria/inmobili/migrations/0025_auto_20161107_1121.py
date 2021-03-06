# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-07 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobili', '0024_auto_20161027_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='bathrooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='casa',
            name='people',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='casa',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='casa',
            name='rooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.FileField(upload_to='casa/', verbose_name='Imagen de la Casa'),
        ),
    ]
