# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.files.storage import FileSystemStorage

# Create your models here.
FS_USER_AVATARS= FileSystemStorage(location=settings.MEDIA_ROOT + "/user-avatars/")


class Casa(models.Model):
    CATEGORIAS = (
        ("0", 'Venta'),
        ("1", 'Alquiler'),
    )
    Operation = models.CharField(max_length=6,
                                 choices=CATEGORIAS,
                                 default="0")
    location = models.CharField(max_length=60)
    district = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    surface = models.CharField(max_length=60)
    free_surface = models.CharField(max_length=60)
    cover_surface = models.CharField(max_length=60)
    rooms = models.CharField(max_length=60)
    bathrooms = models.CharField(max_length=60)
    condition = models.CharField(max_length=60)
    heating = models.CharField(max_length=60)
    description = models.TextField()
    price =  models.CharField(max_length=20)
    img_frente = models.ImageField(upload_to='', null=True)

    def __unicode__(self):
        return self.address


class Perfil(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=256, default="")