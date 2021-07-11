from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'books/detail.html', {'book': book})
