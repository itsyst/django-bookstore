from django_filters.rest_framework import FilterSet
from .models import Book

class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'genre_id': ['exact'],
            'number_in_stock':['gt']
        }