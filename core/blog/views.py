from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import PostForm
from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post

    context_object_name = "posts"
    ordering = "id"
    # paginate_by = 2

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=False)
    #     return posts


class PostDetailView(DeleteView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeletView(DeleteView):
    model = Post
    success_url = "/blog/post/"
    template_name = "blog/delete.html"


@api_view()
def api_post_lits_view(request):
    return Response("hello world")
