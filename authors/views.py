from django.contrib.auth import get_user_model
from django.views import generic

from rest_framework import viewsets

from .models import Author
from .serializers import AuthorSerializer, UserSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
