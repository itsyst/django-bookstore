from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = Book.objects.select_related('genre').all()
        serializer = BookSerializer(queryset, many = True, context = {'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
 
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'GET':
        serializer = BookSerializer(book, context = {'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PATCH':
        serializer = BookSerializer(book, data=request.data, partial=True)  # Allow partial updates
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        if book.number_in_stock > 0:
            return Response({'error': 'Book can not deleted.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.annotate(books_count=Count('books'))
        serializer = GenreSerializer(genres, many = True, context = {'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GenreSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
      
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def genre_detail(request, id):
    genre = get_object_or_404(Genre.objects.annotate(books_count =Count('books')), pk=id)
    if request.method == 'GET':
        serializer = GenreSerializer(genre, context = {'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GenreSerializer(genre, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PATCH':
        serializer = GenreSerializer(genre, data=request.data, partial=True)  # Allow partial updates
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        if genre.books.count() > 0:
            return Response({'error':'Genre cannot be deleted.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
