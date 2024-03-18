from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput,TextInput
from django.contrib.auth.forms import AuthenticationForm



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']




    
    


