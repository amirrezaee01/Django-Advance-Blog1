from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

app_name = 'api-v1'

urlpatterns = [
    path('post/', PostList.as_view(), name='post-list'),
    path('post/<int:id>/', PostDetail, name='post-detail'),

]
