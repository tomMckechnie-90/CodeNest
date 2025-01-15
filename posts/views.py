from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

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
    comments = post.comments.all().order_by("-created_at") # Fetch related comments using the `related_name='comments'`
    comment_count = post.comments.filter(approved=True).count()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been submitted and awaiting approval'
            )
    comment_form = CommentForm()
    return render(request, 
                'posts/post_detail.html', {
                    'post': post, 
                    'comments': comments,
                    'comment_count': comment_count,
                    'comment_form': comment_form,
                    })


def comment_edit(request, comment_id):
    if request.method == "POST":

        # queryset = Post.objects.filter(status=1)
        comment = get_object_or_404(Comment, pk=comment_id)
        post = comment.post
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment has updated')
        else:
            messages.add_message(request, messages.ERROR, 'ERROR! comment was not updated!')

    return HttpResponseRedirect(reverse('post_detail', args=[comment.post.slug]))
