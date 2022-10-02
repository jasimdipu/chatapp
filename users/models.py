from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

from utils.models import BaseModel


class User(AbstractUser, BaseModel):
    email = models.EmailField()
