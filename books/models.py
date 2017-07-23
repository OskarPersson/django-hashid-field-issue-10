from django.db import models

from hashid_field import HashidAutoField


class Book(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    author = models.ForeignKey('authors.Author', on_delete=models.SET_NULL, related_name='books', null=True)
