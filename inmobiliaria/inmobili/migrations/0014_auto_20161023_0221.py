# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-23 02:21
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobili', '0013_auto_20161018_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='satifaccion',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='casa',
            name='img_frente',
            field=models.ImageField(null=True, upload_to=django.core.files.storage.FileSystemStorage(location='/home/rodri/Cole/Programacion3/otro/inmobiliaria/media/casa-images/')),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to=django.core.files.storage.FileSystemStorage(location='/home/rodri/Cole/Programacion3/otro/inmobiliaria/media/casa-images/')),
        ),
    ]
