# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 21:53
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobili', '0019_auto_20161024_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='img_frente',
            field=models.ImageField(default=1, storage=django.core.files.storage.FileSystemStorage(location='/home/rodri/Cole/Programacion3/proyecto final/inmobiliaria/media/donacion-img/'), upload_to=b'', verbose_name='Imagen de la Casa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/rodri/Cole/Programacion3/proyecto final/inmobiliaria/media/donacion-img/'), upload_to=b'', verbose_name='Imagen de la Casa'),
        ),
    ]