from django.urls import path
from rest_framework.routers import SimpleRouter

from user_profile.views import UserProfileViewSet

router = SimpleRouter()

router.register(r"user-profile", UserProfileViewSet, basename="user-profile")

urlpatterns = router.urls
