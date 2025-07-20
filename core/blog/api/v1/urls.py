from rest_framework.routers import DefaultRouter

from .views import *

app_name = "api-v1"

router = DefaultRouter()
router.register(r"post", PostModelViewSet, basename="post")
router.register(r"category", CategoryModelViewSet, basename="category")
urlpatterns = router.urls
