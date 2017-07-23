from hashid_field.rest import HashidSerializerCharField

from rest_framework import serializers

from authors.serializers import AuthorSerializer

from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    id = HashidSerializerCharField(source_field='books.Book.id')
    author = AuthorSerializer()
    #author = serializers.PrimaryKeyRelatedField(pk_field=HashidSerializerCharField(source_field='authors.Author.user'), read_only=True)

    class Meta:
        model = Book
        fields = ('url', 'id', 'name', 'author',)
