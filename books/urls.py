from rest_framework_nested import routers
from .views import GenreViewSet, BookViewSet, CartViewSet,CartItemViewSet,  ReviewViewSet

#Parent routers
router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('genres', GenreViewSet)
router.register('carts', CartViewSet)

#Child routers
books_router = routers.NestedDefaultRouter(router, 'books',lookup='book')
books_router.register('reviews', ReviewViewSet, basename='book-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')  
carts_router.register('items', CartItemViewSet, basename='cart-items')  

#URLConf
urlpatterns = router.urls + books_router.urls + carts_router.urls
  