from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreateForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in as %s' % User.objects.get(email=email))
                # Redirect to a success page.
                return redirect('/')
            else:
                # Return an 'invalid login' error message.
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    context = {'form': form}

    return render(request, 'users/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


def profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {'user': user}

    return render(request, 'users/profile.html', context)

