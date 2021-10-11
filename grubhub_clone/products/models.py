from django.db import models 
from django.contrib.auth.models import User

class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.CharField(max_length=150)

