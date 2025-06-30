from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    # path('post/', PostListView.as_view(), name='post-list'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/create/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    # path('post/<int:pk>/delete', PostDeletView.as_view(), name='post-delete')
    path('post/', api_post_lits_view, name='api-post-list')
]
