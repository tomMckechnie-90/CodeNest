from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Post
# Create your views here.

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'base.html'

def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def post_detail(request, slug):
    # fetches the post by its slug
    # queryset = Post.objects.filter(status=1)
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post_detail.html', {'post': post})


