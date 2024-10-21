from django.shortcuts import get_object_or_404
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
 
from .filters import BookFilter
from .pagination import DefaultPagination
from .models import Book, Cart, CartItem, Genre, Review
from .serializers import AddCartItemSerializer, BookSerializer, CartItemSerializer, CartSerializer, GenreSerializer, ReviewSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('genre').all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['genre_id', 'number_in_stock']
    filterset_class = BookFilter
    search_fields = ['title', 'description']
    ordering_fields = ['number_in_stock', 'last_updated']
    pagination_class = DefaultPagination
    lookup_field = 'id'
   
    def get_serializer_context(self):
        return  {'request': self.request} 
    
    def destroy(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=kwargs['id'])
        if book.number_in_stock > 0:
            return Response({'error': 'Book cannot be deleted as it still has stock available.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.annotate(books_count=Count('books'))  # Annotate books_count here
    serializer_class = GenreSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        genre = get_object_or_404(Genre.objects.annotate(books_count=Count('books')), id=kwargs['id'])
        if genre.books_count > 0:
            return Response({'error': 'Genre cannot be deleted. It has associated books.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_id'])
    
    def get_serializer_context(self):
        return {'book_id': self.kwargs['book_id']}
    
class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__book').all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}
    
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
 