from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import SimpleRouter

from user_profile.views import UserProfileViewSet, UserViewSet

router = SimpleRouter()

router.register(r"user", csrf_exempt(UserViewSet), basename="user")
router.register(r"user-profile", csrf_exempt(UserProfileViewSet), basename="user-profile")

urlpatterns = router.urls
