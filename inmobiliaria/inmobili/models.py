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
    location = models.CharField("Provincia", max_length=60)  
    district = models.CharField("Barrio", max_length=60)
    address = models.CharField("Calle", max_length=60)
    surface = models.CharField("Superficie", max_length=60)
    free_surface = models.CharField("Superficie Libre", max_length=60)
    cover_surface = models.CharField("Superficie cubierta", max_length=60)
    rooms = models.IntegerField("Ambientes", default=1)
    bathrooms = models.IntegerField("Baños", default=1)
    condition = models.CharField("Condicion", max_length=60)
    heating = models.CharField("Calefaccion", max_length=60)
    description = models.TextField("Descripcion")
    price =  models.IntegerField("Precio", default=0)
    people = models.IntegerField("Cantidad de Personas", default=1)
    img_frente = models.ImageField("Imagen de la Casa", upload_to="casa/")

    def __unicode__(self):
        return self.address


class Perfil(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=256, default="")
    
    
class Comment(models.Model):
    casa = models.ForeignKey(Casa, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.CharField(max_length=600)
    
    def __unicode__(self):
        return self.body
    
class Image(models.Model):
<<<<<<< HEAD
    casa = models.ForeignKey(Casa, null=True, on_delete=models.CASCADE)
=======
    casa = models.ForeignKey(Casa, null=True)
>>>>>>> 7b4ebed10570026eb461e8d79b14b595bea05bb6
    img = models.FileField("Imagen de la Casa", upload_to="casa/")
    

class Fav(models.Model):
    author = models.CharField(max_length=60)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)
