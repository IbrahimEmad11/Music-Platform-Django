from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.CharField(max_length=256 , blank=True, null=True)
    username = models.CharField(max_length=32 , unique =True)
    email = models.EmailField(max_length=64)
    password1 =models.CharField(max_length=32)
    password2 =models.CharField(max_length=32)

    USERNAME_FIELD = 'username'