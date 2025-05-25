from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    path('cbv-index', Indexview.as_view(), name='cbv-index'),
    path('go-google', GoogleView.as_view(), name='go-google'),
    path('posts/', PostListView.as_view(), name='posts')
]
