from django.db import models

# Create your models here.
class hermanas(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    nacimiento=models.CharField(max_length=8)

class padres(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    nacimiento=models.CharField(max_length=8)
