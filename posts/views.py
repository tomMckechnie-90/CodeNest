from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from .forms import PostForm

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



def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment has been deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[comment.post.slug]))


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Your post has been published!')
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'posts/create_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug) # sends you back to the post detail page once edited
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post}) # Pass post to template


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST': # Confirm you want to delete
        post.delete()
        return redirect('home') # Rerturns to the list of posts
    return render(request, 'posts/delete_post.html', {'post': post})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user) # Unlike if post is liked
    else:
        post.likes.add(request.user) # User can like the post
    
    return redirect('post_detail', slug=post.slug)





