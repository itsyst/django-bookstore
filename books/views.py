from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Book, Genre, Review
from .serializers import BookSerializer, GenreSerializer, ReviewSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('genre').all()
    serializer_class = BookSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        return  {'request': self.request} 
    
    def destroy(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=kwargs['id'])
        if book.number_in_stock > 0:
            return Response({'error': 'Book cannot be deleted as it still has stock available.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.annotate(books_count=Count('books'))  # Annotate books_count here
    serializer_class = GenreSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        genre = get_object_or_404(Genre.objects.annotate(books_count=Count('books')), id=kwargs['id'])
        if genre.books_count > 0:
            return Response({'error': 'Genre cannot be deleted. It has associated books.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_id'])
    
    def get_serializer_context(self):
        return {'book_id': self.kwargs['book_id']}