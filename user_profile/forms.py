from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from password.models import Passwords
from user_profile.models import Site

class RegisterForm( UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class PasswordForm(forms.ModelForm):
    # model = Passwords
    class Meta:
        model= Passwords
        fields = '__all__'

class SiteForm(forms.ModelForm):
    class Meta:
        model= Site
        exclude = ('user',)