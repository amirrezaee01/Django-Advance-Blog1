from django.urls import include, path

from .views import *

app_name = "blog"

urlpatterns = [
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", PostEditView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete", PostDeletView.as_view(), name="post-delete"),
    path("api/v1/", include("blog.api.v1.urls")),
]
