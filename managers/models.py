from django.db import models

# Create your models here.
class Manager(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=20)
    correo=models.EmailField(blank=True,null=True)
    edad=models.IntegerField(null=True)

    def __str__(self):
        return self.nombre


