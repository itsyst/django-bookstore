from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='books')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
