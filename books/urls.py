from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('genres', views.GenreViewSet)
router.register('', views.BookViewSet)
 
#URLConf
urlpatterns = router.urls
  