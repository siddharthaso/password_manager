from django.shortcuts import redirect, render
# from .forms import loginForm
# from .forms import signupForm
from django.contrib import messages

from .forms import RegisterForm
from password.forms import PasswordForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created ')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'user_profile/register.html',{'form':form})

# Create your views here.
def home(request):
    return render(request, 'home.html')