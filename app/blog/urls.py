from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()

router.register("blog", BlogViewSet, basename="blogs")

urlpatterns = router.urls
