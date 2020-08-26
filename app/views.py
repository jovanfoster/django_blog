from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import *

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'app/index.html', context)


class PostDetail(DetailView):
    model = Post