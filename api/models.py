from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField
    age = models.IntegerField

    def __str__(self):
        return self.name