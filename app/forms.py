from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'body']


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'body']