from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ...models import Category, Post
from .paginations import LargeResultsSetPagination
from .permissions import IsOwnerOrReadOnly
from .serializer import CategorySerializer, PostSerializer


class PostModelViewSet(viewsets.ModelViewSet, IsOwnerOrReadOnly):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author", "status"]
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = LargeResultsSetPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
