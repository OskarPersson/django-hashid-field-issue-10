from django.conf import settings
from django.contrib.auth import get_user_model
from hashid_field.rest import HashidSerializerCharField
from rest_framework import serializers
from .models import Author


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = HashidSerializerCharField(source_field='%s.id' % settings.AUTH_USER_MODEL)

    class Meta:
        model = get_user_model()
        fields = ('url', 'id', 'username')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Author
        fields = ('url', 'user', 'description',)
