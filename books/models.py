from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    ISBN = models.IntegerField(max_length=13)
    title = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
