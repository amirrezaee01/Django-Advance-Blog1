from django.urls import path, include
from .views import *
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register(r'post', PostModelViewSet, basename='post')
router.register(r'category', CategoryModelViewSet, basename='category')
urlpatterns = router.urls

# urlpatterns = [
#     path('post/', PostList.as_view(), name='post-list'),
#     path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),

# ]
# urlpatterns += router.urls
