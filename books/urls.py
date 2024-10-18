from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path('', views.BookList.as_view(), name='index'),
    path('<int:id>', views.BookDetail.as_view()),
    path('genres', views.GenreList.as_view(), name='genre_list'),
    path('genres/<int:id>', views.GenreDetail.as_view(), name='genre-detail'),
]
