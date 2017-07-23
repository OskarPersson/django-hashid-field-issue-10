from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from authors.views import AuthorViewSet, UserViewSet
from books.views import BookViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
