from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body']


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['body']


