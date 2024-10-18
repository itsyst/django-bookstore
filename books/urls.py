from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path('', views.book_list, name='index'),
    path('<int:id>', views.book_detail),
    path('genres', views.genre_list, name='genre_list'),
    path('genres/<int:id>', views.genre_detail, name='genre-detail'),
]
