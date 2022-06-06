from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from password.forms import PasswordLogicForm
from password.utils import generate_pwd
from password.forms import PasswordForm
from password.models import Passwords

from .forms import RegisterForm, SiteForm
from .models import Profile, Site, Tags


class RegisterView(SuccessMessageMixin,CreateView):
    form_class =  RegisterForm
    template_name = "user_profile/register.html"
    success_url = reverse_lazy('user_profile:login')

    def get_success_message(self, cleaned_data):
        return f"Welcome {self.object.username.capitalize()}, Your Account is Successfully Created!"


class HomeView(CreateView):
    form_class = PasswordLogicForm
    success_url = reverse_lazy('password:generate_pwd')
    form1 = PasswordLogicForm()
    form2 = PasswordForm()
    
    def get(self, request , *args, **kwargs):
        context = {'form1':self.form1, 'form2': self.form2 }
        return render(request, 'home.html', context = context)

    def post(self, request, *args, **kwargs):
        
        print("data",request.POST)

        if 'form1' in request.POST:
            form1 = PasswordLogicForm(request.POST)
            form2 = PasswordForm(request.POST)

            if form1.is_valid():
                pwd = generate_pwd(int(request.POST.get('length')), bool(request.POST.get('uppercase')),bool(request.POST.get('lowercase')),bool(request.POST.get('numbers')),bool(request.POST.get('symbols')),bool(request.POST.get('extra_symbols')))
                context = {'pwd':pwd}
                return render(request, 'home.html',context=context)

            context = context = {'form1':form1, 'form2': form2 }
            return render(request, 'home.html',context=context)

        elif 'form2' in request.POST:

            if request.user.is_authenticated:
                mypwd = request.POST['pwd']
                myus = request.user
                obj = Passwords(password = mypwd, user = myus)
                obj.save()
                return redirect('password:view_pwd')

            return redirect('user_profile:login')
        
        return redirect('user_profile:home')

#view user profile
@login_required(login_url='user_profile:login')
def profile(request):
    user = User.objects.get(username = request.user)
    profile = Profile.objects.get(user= user)
    context = {'user' : user, 'profile' : profile}
    return render(request, 'user_profile/profile.html',context = context)


class CreateSiteView(LoginRequiredMixin, CreateView):
    template_name = 'create_site.html'
    form_class = SiteForm
    login_url = 'user_profile:login'
    success_url = reverse_lazy('user_profile:home')
    success_message = "Site Created Successfully!"

    def get(self, request , *args, **kwargs):
        form = SiteForm(request.POST)
        context = {'form':form}
        return render(request, 'user_profile/add_site.html',context=context)

    def post(self, request, *args, **kwargs):
        myus = request.user
        obj = Site.objects.create(site_name =request.POST['site_name'], site_url = request.POST['site_url'], is_private = bool(request.POST.get('is_public',None)),  user = myus)
        obj.save()
        messages.success(self.request, self.success_message)
        return redirect('user_profile:home')

class TagsCreateView(LoginRequiredMixin, CreateView):
    model = Tags
    template_name = "user_profile/create_tag.html"
    fields = ['tags_name']
    login_url = 'user_profile:login'
    success_url = reverse_lazy('user_profile:home')
    success_message = "Tag Created Successfully!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy('user_profile:home')

    def form_valid(self, form):
        ob = form.save(commit=False)
        ob.user = self.request.user
        return super().form_valid(ob)

from .tasks import download_user
def dowuser(self):
    # return download_user()
    download_user.delay()
    return HttpResponse( "<h1>Downloaded Successfully</h1>")