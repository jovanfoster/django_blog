from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class UserCreateForm(UserCreationForm):
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password']