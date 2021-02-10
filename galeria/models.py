from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Imagen(models.Model):
    imagen = models.ImageField(upload_to = 'galeria')
    nombre = models.CharField(max_length=200)

    
