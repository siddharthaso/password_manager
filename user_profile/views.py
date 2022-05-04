from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import RegisterForm, SiteForm
from .models import Profile, Site, Tags


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'user_profile/login.html'
    # success_url = '/success_url/'
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
            return redirect('user_profile:home')
    else:
        form = RegisterForm()
    return render(request, 'user_profile/register.html',{'form':form})


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def profile(request):
    user = User.objects.get(username = request.user)
    profile = Profile.objects.get(user= user)
    context = {'user' : user, 'profile' : profile}
    return render(request, 'user_profile/profile.html',context = context)


class CreateSiteView(CreateView):
    template_name = 'create_site.html'
    form_class = SiteForm
    success_url = reverse_lazy('user_profile:home')

    def get(self, request , *args, **kwargs):

        form = SiteForm(request.POST)
        context = {'form':form}
        return render(request, 'user_profile/add_site.html',context=context)
    
    def post(self, request, *args, **kwargs):
        myus = request.user
        obj = Site.objects.create(site_name =request.POST['site_name'], site_url = request.POST['site_url'], is_public = bool(request.POST['is_public']),  user = myus)
        obj.save()
        
        return render(request, 'home.html')


class TagsCreateView(CreateView):
    model = Tags
    template_name = "user_profile/create_tag.html"
    fields = '__all__'
    success_url = reverse_lazy('user_profile:home')
    
# class TagsDetailView(DetailView):
#     model = Tags
#     template_name = ".html"
# )