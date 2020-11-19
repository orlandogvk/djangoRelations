from django.db import models
from areas.models import Area
from managers.models import Manager

# Create your models here.

class Empleado(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    cargo=models.CharField(max_length=150)

    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    managers = models.ManyToManyField(Manager, related_name='empleados')


