from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    gender_choice = ((0, 'female'), (1, 'male'), (2, 'unknown'))
    gender = models.IntegerField(choices=gender_choice, default=0)
    age = models.IntegerField(default=0)
    address = models.CharField(default='', max_length=255)

# Create your models here.
