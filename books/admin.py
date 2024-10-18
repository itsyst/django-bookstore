from django.utils.html import format_html, urlencode
from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from books import models
 
@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'books_count')
    list_editable = ['name']

    @admin.display(ordering="books_count")
    def books_count(self, genre):
        url = (reverse('admin:books_book_changelist')
               + '?'
               + urlencode(
                 {'genre__id': str(genre.id)}
        ))
        return format_html('<a href="{}">{}</a>', url, genre.books_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(books_count = Count('books'))

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('ISBN', 'title', 'description',
                    'number_in_stock', 'daily_rate')
    
    list_editable = ['number_in_stock']
    search_fields = ['ISBN', 'title']
    list_per_page = 10
 