from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_restaurant_owner = models.BooleanField(default=False)