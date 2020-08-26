from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import *
from .forms import *


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'app/index.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()

    context = {'form': form}
    
    return render(request, 'app/post_create_form.html', context)


def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    
    return render(request, 'app/post_update_form.html', context)


class PostDetail(DetailView):
    model = Post