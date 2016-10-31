## Buscar minimal django file upload example
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import admin
#from django.core.files.storage import FileSystemStorage

# Create your models here.

class Casa(models.Model):
    CATEGORIAS = (
        ('Venta', 'Venta'),
        ('Alquiler', 'Alquiler'),
    )
    Operation = models.CharField(max_length=16,
                                 choices=CATEGORIAS,
                                 default=0)
    CATEGORIAS1 = (
        ('Departamento', 'Departamento'),
        ('Casa', 'Casa'),
        ('Oficina', 'Oficina'),
    )
    tipo = models.CharField(max_length=16,
                            choices=CATEGORIAS1,
                            default=1)
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
    people = models.CharField(max_length=60)
    img_frente = models.ImageField("Imagen de la Casa", upload_to="casa/")

    def __unicode__(self):
        return self.address


class Perfil(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=256, default="")
    
    
class Comment(models.Model):
    casa = models.ForeignKey(Casa, null=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.CharField(max_length=600)
    
    def __unicode__(self):
        return self.body
    
class Image(models.Model):
    casa = models.OneToOneField(Casa, on_delete=models.CASCADE)
    img = models.FileField("Imagen de la Casa", upload_to="casa/")
    

class Fav(models.Model):
    author = models.CharField(max_length=60)
    casa = models.OneToOneField(Casa, on_delete=models.CASCADE)
