# Generated by Django 5.1.2 on 2024-10-19 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_genre_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]