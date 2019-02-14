from django.urls import path, include
from .views import AuthorView, AuthorDetailView, BookView, BookDetailView, SearchView

urlpatterns = [
    path('authors/', AuthorView.as_view(), name='authors'),
    path('authors/<slug>/', AuthorDetailView.as_view(), name='author'),
    path('books/', BookView.as_view(), name='books'),
    path('books/<book_name>/', BookDetailView.as_view(), name='book'),
    path('search/', SearchView.as_view(), name='search'),
]
