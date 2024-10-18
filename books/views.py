from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer

class BookList(ListCreateAPIView): 
    queryset = Book.objects.select_related('genre').all()
    serializer_class = BookSerializer
    
    def get_serializer_context(self):
        return  {'request': self.request} 
 
class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related('genre').all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    
    def get_serializer_context(self):
        return {'request': self.request}
 
    def delete(self, request, id):
        book = get_object_or_404(Book, pk=id)
        if book.number_in_stock > 0:
            return Response({'error': 'Book can not deleted.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
class GenreList(ListCreateAPIView):
    queryset = Genre.objects.annotate(books_count=Count('books'))  # Annotate books_count here
    serializer_class = GenreSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class GenreDetail(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.annotate(books_count=Count('books'))  # Annotate books_count here
    serializer_class = GenreSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        return {'request': self.request}

    def delete(self, request, id):
        genre = get_object_or_404(Genre.objects.annotate(books_count=Count('books')), pk=id)
        if genre.books_count > 0:
            return Response({'error': 'Genre cannot be deleted. It has associated books.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)