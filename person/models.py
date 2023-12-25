from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
