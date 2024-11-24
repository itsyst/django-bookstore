from django.db import transaction
from rest_framework import serializers
from .signals import order_created
from .models import Book, BookImage, Cart, CartItem, Customer, Genre, Order, OrderItem, Review

class GenreSerializer(serializers.ModelSerializer):
    books_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Genre
        fields = ['id','name', 'books_count']
    
class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id','image']
    
    def create(self, validated_data):
        book_id = self.context['book_id']
        return BookImage.objects.create(book_id = book_id, **validated_data)
    
class BookSerializer(serializers.ModelSerializer):
    images = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'description', 'number_in_stock', 'daily_rate', 'unit_price', 'date_created', 'genre', 'images']
   
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'date']

    def create(self, validated_data):
        book_id = self.context['book_id']
        return Review.objects.create(book_id=book_id, **validated_data)

class BookSelectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'unit_price']

class AddCartItemSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['id' , 'book_id', 'quantity']


    def validate_book_id(self, value):
        if not Book.objects.filter(pk=value).exists():
            raise serializers.ValidationError('No book with the given Id was found.')
        return value
        
    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        book_id = self.validated_data['book_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, book_id=book_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
 
        return self.instance
        
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
         model = CartItem
         fields = ['quantity']

class CartItemSerializer(serializers.ModelSerializer):
    book = BookSelectiveSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'book', 'quantity', 'total_price']


    def get_total_price(self, cart_item:CartItem):
        return cart_item.quantity * cart_item.book.unit_price

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id','items', 'total_price']

    def get_total_price(self, cart):
        cards = cart.items.all()
        return sum([ item.quantity * item.book.unit_price for item in cards])
 
class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True) 

    class Meta:
        model = Customer
        fields =['id', 'user_id', 'phone', 'birth_date']

class OrderItemSerializer(serializers.ModelSerializer):
    book = BookSelectiveSerializer()

    class Meta:
        model = OrderItem
        fields =['id', 'book', 'unit_price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many = True)

    class Meta:
        model = Order
        fields =['id', 'placed_at', 'payment_status', 'customer', 'items']

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():    
            raise serializers.ValidationError('No cart with the given id is found.')
        if CartItem.objects.filter(cart_id = cart_id).count() == 0:
            raise serializers.ValidationError('The cart is empty.')
        return cart_id
    
    def save(self, **kwargs):
        with transaction.atomic():
             cart_id = self.validated_data['cart_id']
             customer = Customer.objects.get(user_id =self.context['user_id'])
             order = Order.objects.create(customer = customer)

             cart_items = CartItem.objects.select_related('book').filter(cart_id = cart_id)
             
             order_items =[
                 OrderItem (
                    order = order,
                    book = item.book,
                    unit_price = item.book.unit_price,
                    quantity = item.quantity
                )for item in cart_items
             ]
             OrderItem.objects.bulk_create(order_items)

             Cart.objects.filter(pk=cart_id).delete()

             order_created.send_robust(self.__class__, order=order)

        return order
    
class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']
