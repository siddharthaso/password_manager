from django import forms
from .models import Passwords

class PasswordForm(forms.ModelForm):
    # model = Passwords
    class Meta:
        model= Passwords
        fields = ['password']

class PasswordAllFieldForm(forms.ModelForm):
    # model = Passwords
    class Meta:
        model= Passwords
        fields = '__all__'

# class PasswordForm(forms.ModelForm):
#     class Meta:
#         model = Passwords
#         exclude = ('user',)