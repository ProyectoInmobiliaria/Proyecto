# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 22:00
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobili', '0020_auto_20161024_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='img_frente',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/rodri/Cole/Programacion3/proyecto final/inmobiliaria/media/Casa-img/'), upload_to=b'', verbose_name='Imagen de la Casa'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/rodri/Cole/Programacion3/proyecto final/inmobiliaria/media/Casa-img/'), upload_to=b'', verbose_name='Imagen de la Casa'),
        ),
    ]