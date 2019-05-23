from django.db import models

# Create your models here.
class User(models.Model):
    user_date = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_photo = models.CharField(max_length=30)
