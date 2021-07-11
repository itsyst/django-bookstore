from django.db import models
from tastypie.resources import ModelResource
from books.models import Book


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'books'
