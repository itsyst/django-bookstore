from books.models import Book, Genre
from rest_framework import serializers

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'books_count']
    
    books_count = serializers.IntegerField(read_only=True)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'description', 'number_in_stock', 'daily_rate', 'date_created', 'genre']

    