from rest_framework import serializers
from .models import Book, Cart, CartItem, Genre, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'books_count']
    
    books_count = serializers.IntegerField(read_only=True)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'description', 'number_in_stock', 'daily_rate', 'unit_price', 'date_created', 'genre']

 
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

class CartItemSerializer(serializers.ModelSerializer):
    book = BookSelectiveSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item:CartItem):
        return cart_item.quantity * cart_item.book.unit_price
 
    class Meta:
        model = CartItem
        fields = ['id', 'book', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        cards = cart.items.all()
        return sum([ item.quantity * item.book.unit_price for item in cards])
    
    class Meta:
        model = Cart
        fields = ['id','items', 'total_price']


