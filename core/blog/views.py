from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.views.generic.list import ListView
# Create your views here.


def indexview(request):
    return render(request, 'index.html')


class Indexview(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'amir'
        context['posts'] = Post.objects.all()
        return context


class GoogleView(RedirectView):
    url = 'https://www.google.com'


class PostListView(ListView):
    model = Post

    context_object_name = 'posts'
    ordering = 'id'
    paginate_by = 2

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=False)
    #     return posts
