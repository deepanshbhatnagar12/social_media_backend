from django.urls import path
from rest_framework.routers import SimpleRouter

from user_profile.views import UserProfileViewSet, UserViewSet, TagViewSet, InterestViewSet

router = SimpleRouter()

router.register(r"user", UserViewSet, basename="user")
router.register(r"user-profile", UserProfileViewSet, basename="user-profile")
router.register(r"sm-interests", InterestViewSet, basename="sm-interests")
router.register(r"sm-tags", TagViewSet, basename="sm-tags")


urlpatterns = router.urls
