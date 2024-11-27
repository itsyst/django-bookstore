from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework_nested import routers
from .views import (
    BookImageViewSet,
    CartItemViewSet,
    BookViewSet,
    CartViewSet,
    CustomerViewSet,
    GenreViewSet,
    OrderViewSet,
    SendEmailViewSet,
    ReviewViewSet
)

#Parent routers
router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('genres', GenreViewSet)
router.register('carts', CartViewSet)
router.register('customers', CustomerViewSet)
router.register('orders', OrderViewSet, basename='orders')
router.register('messages', SendEmailViewSet, basename='messages')   

#Child routers
books_router = routers.NestedDefaultRouter(router, 'books',lookup='book')
books_router.register('reviews', ReviewViewSet, basename='book-reviews')
books_router.register('images', BookImageViewSet, basename='book-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')  
carts_router.register('items', CartItemViewSet, basename='cart-items')  
  
# URLConf
urlpatterns = router.urls + books_router.urls + carts_router.urls

# Static and media files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]