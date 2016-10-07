# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

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

    def __unicode__(self):
        return self.address


    class UserProfile(models.Model):
        user   = models.OneToOneField(User)
        avatar = models.ImageField()