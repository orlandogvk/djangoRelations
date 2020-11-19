from django.db import models

# Create your models here.
class Area(models.Model):
    descripcion=models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    telefono=models.CharField(max_length=20)

    created=models.DateTimeField(auto_now_add=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)

