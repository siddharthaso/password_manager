from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm( UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

from password.models import Passwords

class PasswordForm(forms.ModelForm):
    # model = Passwords
    class Meta:
        model= Passwords
        fields = '__all__'
