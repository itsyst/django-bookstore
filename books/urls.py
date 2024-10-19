from rest_framework_nested import routers
from .views import GenreViewSet, BookViewSet, ReviewViewSet

#Parent routers
router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('genres', GenreViewSet)

#Child routers
books_router = routers.NestedDefaultRouter(router, 'books',lookup='book')
books_router.register('reviews', ReviewViewSet, basename='book-reviews')

  
#URLConf
urlpatterns = router.urls + books_router.urls
  