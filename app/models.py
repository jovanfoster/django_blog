from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    body = models.TextField()   
    date_created = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=30)
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)   
    date_created = models.TimeField(auto_now=True)

