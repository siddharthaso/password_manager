from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
# from .forms import loginForm
# from .forms import signupForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from password.forms import PasswordForm
from django.contrib.auth.models import User
from .models import Profile


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'user_profile/login.html'
    success_url = '/s/'
    success_message = "You were successfully logged in."

class LogoutFormView(SuccessMessageMixin, LogoutView):
    template_name = 'user_profile/logout.html'
    # success_url = '/success_url/'
    success_message = "Successfully logged out."

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

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def profile(request):
    user = User.objects.get(username = request.user)
    # profile = Profile.objects.filter(user=user).first()
    # if profile is None:
    #     print("not have profile")
    profile = Profile.objects.get(user= user)
    context = {'user' : user, 'profile' : profile}
    return render(request, 'user_profile/profile.html',context = context)