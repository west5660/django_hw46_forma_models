from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()

class Car(models.Model):
    marka = models.CharField(max_length=15)
    proizv = models.CharField(max_length=15)
    age = models.IntegerField()
    gn = models.CharField(max_length=15)

