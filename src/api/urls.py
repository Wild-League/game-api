from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

router = SimpleRouter()
router.register('decks', views.DeckModelViewSet)

urlpatterns = [
	path(r'auth/signin/', TokenObtainPairView.as_view()),
	path(r'auth/signup/', csrf_exempt(views.AuthModelViewSet.as_view({ 'post': 'signup' }))),
]

urlpatterns += router.urls
