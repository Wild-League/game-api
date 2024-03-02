from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('decks', views.DeckModelViewSet)

urlpatterns = router.urls
