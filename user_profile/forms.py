from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from user_profile.models import Site

class RegisterForm( UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class SiteForm(forms.ModelForm):
    class Meta:
        model= Site
        exclude = ('user',)