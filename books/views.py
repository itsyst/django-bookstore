from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer

class BookList(APIView):
    def get(self, request): 
        queryset = Book.objects.select_related('genre').all()
        serializer = BookSerializer(queryset, many = True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
 
class BookDetail(APIView):
    def get(sef, request, id):
        book = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(book, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request, id):
        book = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(book, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def patch(self, request, id):
        book = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(book, data=request.data, partial=True)  # Allow partial updates
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        book = get_object_or_404(Book, pk=id)
        if book.number_in_stock > 0:
            return Response({'error': 'Book can not deleted.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.annotate(books_count=Count('books'))
        serializer = GenreSerializer(genres, many = True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GenreSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
      
class GenreDetail(APIView):
    def get(self, request, id):
        genre = get_object_or_404(Genre.objects.annotate(books_count =Count('books')), pk=id)
        serializer = GenreSerializer(genre, context = {'request': request})
        return Response(serializer.data)

    def post(self, request, id):
        genre = get_object_or_404(Genre.objects.annotate(books_count =Count('books')), pk=id)
        serializer = GenreSerializer(genre, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, id):
        genre = get_object_or_404(Genre.objects.annotate(books_count =Count('books')), pk=id)
        serializer = GenreSerializer(genre, data=request.data, partial=True)  # Allow partial updates
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        genre = get_object_or_404(Genre.objects.annotate(books_count =Count('books')), pk=id)
        if genre.books.count() > 0:
            return Response({'error':'Genre cannot be deleted.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
