from django.conf import settings
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField(max_length=1000)
