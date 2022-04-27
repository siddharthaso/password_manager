from django import forms
from .models import Passwords

class PasswordForm(forms.ModelForm):
    # model = Passwords
    class Meta:
        model= Passwords
        fields = '__all__'
