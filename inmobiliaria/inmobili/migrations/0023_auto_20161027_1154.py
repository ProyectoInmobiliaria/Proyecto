# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-27 11:54
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobili', '0022_auto_20161027_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='img_frente',
            field=models.ImageField(upload_to=django.core.files.storage.FileSystemStorage(location='/home/rodri/Cole/Programacion3/proyecto final/inmobiliaria/media/casa_img/'), verbose_name='Imagen de la Casa'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to=django.core.files.storage.FileSystemStorage(location='/home/rodri/Cole/Programacion3/proyecto final/inmobiliaria/media/casa_img/'), verbose_name='Imagen de la Casa'),
        ),
    ]