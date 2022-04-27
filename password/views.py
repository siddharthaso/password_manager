from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import PasswordForm

# Create your views here.
@login_required


def save_pwd(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, You have stored the password successfully.')
            return redirect('home')
    else:
        
        form = PasswordForm()
    return render(request, 'password/save_password.html',{'form':form})