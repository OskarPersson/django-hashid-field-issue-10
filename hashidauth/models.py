from django.contrib.auth.models import AbstractUser
from django.db import models

from hashid_field import HashidAutoField


class User(AbstractUser):
    id = HashidAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
