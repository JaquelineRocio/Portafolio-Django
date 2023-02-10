from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    last_name=forms.CharField(label="Apellidos",max_length=80)
    first_name=forms.CharField(label="Nombres",max_length=80)
    class Meta:
        model=User 
        fields=['last_name','first_name','username','email','password1','password2']

class LoginForm(forms.Form):

    username = forms.CharField(label="Username", max_length=200, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(label="Password", max_length=200, required=True,widget=forms.PasswordInput(attrs={'class': 'form-control'}))



