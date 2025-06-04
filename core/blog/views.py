from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.views.generic import ListView, DeleteView, CreateView
from .models import Post
from .forms import PostForm
# Create your views here.


class PostListView(ListView):
    model = Post

    context_object_name = 'posts'
    ordering = 'id'
    # paginate_by = 2

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=False)
    #     return posts


class PostDetailView(DeleteView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'
