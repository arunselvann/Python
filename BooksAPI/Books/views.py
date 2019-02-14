from rest_framework import generics, views
from .serializers import *
from .models import Author, Book
from rest_framework.response import Response


class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'slug'


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'book_name'


class SearchView(views.APIView):

    def post(self, request):
        field_name = request.data.get('field_name') + '__icontains'
        field_value = request.data.get('field_value')
        books = Book.objects.filter(**{field_name: field_value})
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)
