from rest_framework import serializers
from .models import Book, Genre, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'books_count']
    
    books_count = serializers.IntegerField(read_only=True)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'description', 'number_in_stock', 'daily_rate', 'date_created', 'genre']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'book', 'date'] 
