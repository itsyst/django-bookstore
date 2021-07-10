from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Genre, Book


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BookAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('ISBN', 'title', 'description',
                    'number_in_stock', 'daily_rate')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
