from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models
 
@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'books_count')
    list_editable = ['name']
    search_fields = ['name']
 
    @admin.display(ordering="books_count")
    def books_count(self, genre):
        url = (reverse('admin:store_book_changelist')
               + '?'
               + urlencode(
                 {'genre__id': str(genre.id)}
        ))
        return format_html('<a href="{}">{}</a>', url, genre.books_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(books_count = Count('books'))

class BookImageInline(admin.TabularInline):
    model = models.BookImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail">') 
        return ''

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    autocomplete_fields = ['genre']
    exclude = ('date_created',)
    list_display = ('ISBN', 'title', 'description',
                    'number_in_stock', 'unit_price', 'daily_rate')
    inlines = [BookImageInline]
    list_editable = ['unit_price']
    list_filter = ['genre', 'last_updated']
    search_fields = ['ISBN', 'title']
    list_select_related = ['genre']
    list_per_page = 10

    class Media:
        css = {
            'all' : ['store/styles.css']
        }
 
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'orders']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )

class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['book']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']