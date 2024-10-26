from django.shortcuts import get_object_or_404
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .permissions import IsAdminOrReadOnly, ViewCustomerHistoryPermissions
from .filters import BookFilter
from .pagination import DefaultPagination
from .models import Book, Cart, CartItem, Customer, Genre, Order, OrderItem, Review
from .serializers import AddCartItemSerializer, BookSerializer, CartItemSerializer, CartSerializer, CreateOrderSerializer, CustomerSerializer, GenreSerializer, OrderItemSerializer, OrderSerializer, UpdateCartItemSerializer,  ReviewSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('genre').all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'description']
    ordering_fields = ['number_in_stock', 'last_updated']
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'id'
   
    def get_serializer_context(self):
        return  {'request': self.request} 
    
    def destroy(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=kwargs['id'])
        if book.number_in_stock > 0:
            return Response({'error': 'Book cannot be deleted as it still has stock available.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.annotate(books_count=Count('books'))  # Annotate store_count here
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'id'

    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        genre = get_object_or_404(Genre.objects.annotate(books_count=Count('books')), id=kwargs['id'])
        if genre.books_count > 0:
            return Response({'error': 'Genre cannot be deleted. It has associated store.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
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
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}
    
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
 
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]
    
    @action(detail=False, permission_classes=[ViewCustomerHistoryPermissions])
    def history(self, request):
        return Response('Ok')
    
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        if request.method == 'GET':
            (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(
            data = request.data,
            context = { 'user_id' : self.request.user.id}
            )
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        
        return Response(serializer.data)
        
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer
    
    def get_queryset(self):
        user = self.request.user

        if user.is_staff: 
            return Order.objects.all()
        
        (customer_id, created) = Customer.objects.only('id').get_or_create(user_id = user.id)
        return Order.objects.filter(customer_id = customer_id)

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

