from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    """Custom logout view that redirects to home page"""
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('library:home')


@login_required
def profile(request):
    """User profile view"""
    user_reviews = request.user.review_set.all()[:5]  # Latest 5 reviews
    return render(request, 'accounts/profile.html', {
        'user_reviews': user_reviews
    })
