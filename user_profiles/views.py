from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User


# Create your views here.

def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(
        request, 'user_profiles/profile.html', {'profile_user': user})


@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Your Profile has been updated.')
            return redirect('view_profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user_profiles/edit_profile.html', {'form': form})
