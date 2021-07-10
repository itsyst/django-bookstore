from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Genre, Book


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Book)
