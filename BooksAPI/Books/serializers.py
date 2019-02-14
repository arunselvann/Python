from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(view_name='author',
                                               lookup_field='slug')

    class Meta:
        model = Author
        fields = ('url', 'id', 'author_name', 'about_author', 'date_of_birth', 'age', 'genre',
                  'website', 'education', 'country', 'occupation', 'author_image',
                  'country', 'occupation', 'author_image')

    def create(self, validated_data):
        try:
            author_instance = Author.objects.get(author_name=validated_data["author_name"])
        except Author.DoesNotExist:
            author_instance, __ = Author.objects.get_or_create(**validated_data)
        return author_instance


class PartialAuthorSerializer(AuthorSerializer):

    class Meta:
        model = Author
        fields = ('author_name', 'url')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    author = PartialAuthorSerializer()
    book_url = serializers.HyperlinkedIdentityField(view_name='book',
                                                    lookup_field='book_name')


    class Meta:
        model = Book
        fields = ('book_url', 'id', 'book_name', 'about_book', 'genre', 'No_of_pages',
                  'language', 'book_image', 'author')

    def create(self, validated_data):
        # author = validated_data.pop('author')
        # try:
        #     author_instance = Author.objects.get(author_name=author['author_name'])
        # except Author.DoesNotExist:
        #     author_instance, __ = Author.objects.get_or_create(**author)
        # validated_data['author'] = author_instance
        try:
            book_instance = Book.objects.get(book_name=validated_data["book_name"])
        except Book.DoesNotExist:
            book_instance, __ = Book.objects.get_or_create(**validated_data)
        return book_instance
