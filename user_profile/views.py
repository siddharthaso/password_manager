from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import CreateView
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

class RegisterView(SuccessMessageMixin, CreateView):
    
    form_class =  RegisterForm
    template_name = "user_profile/register.html"
    success_url = reverse_lazy('user_profile:home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = self.request.user.username
            # messages.success(self.request, f'Welcome {username}, your account is created ')
            success_message = f'Welcome {username}, your account is created '
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        ob = form.save(commit=False)
        return super().form_valid(ob)

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Welcome {username}, your account is created ')
#             return redirect('user_profile:home')
#     else:
#         form = RegisterForm()
#     return render(request, 'user_profile/register.html',{'form':form})

class RegisterView(SuccessMessageMixin,CreateView):

    form_class =  RegisterForm
    template_name = "user_profile/register.html"
    success_url = reverse_lazy('user_profile:home')

    def get_success_message(self, cleaned_data):
        return f"Welcome {self.object.username},Account is successfully created!"

# class RegisterView(SuccessMessageMixin, CreateView):

#     def get(self, request , *args, **kwargs):
#         form = RegisterForm
#         return render(request, 'user_profile/register.html',{'form':form})
        
#     def post(self, request, *args, **kwargs):
#         myus = request.user
#         form = RegisterForm(request.POST)
#         form.save()
#         print(request.POST)
#         username = self.request.POST['username']
#         # print(username)
#         success_message = messages.success(request, f'Welcome {username}, your account is created ')

#         return render(request, 'user_profile/register.html',{'form':form,'messages':[success_message]})

#     def get_success_message(self, cleaned_data):
#         username = self.request.POST['username']
#         success_message = f'Welcome {username}, your account is created '
#         return success_message
    
# class RegisterView(CreateView):
#     template_name = 'user_profile/register.html'
#     context_object_name = 'form'
#     form_class = RegisterForm
#     success_url = reverse_lazy('user_profile:home')
#     def form_valid(self, RegisterForm):
#         """If the form is valid, save the associated model."""
#         self.object = form.save()
#         return super().form_valid(form)
#     def get(self, request , *args, **kwargs):
#         form = SiteForm(request.POST)
#         context = {'form':form}
#         return render(request, 'user_profile/add_site.html',context=context)
#     def post(self, request, *args, **kwargs):
#         myus = request.user
#         obj = Site.objects.create(site_name =request.POST['site_name'], site_url = request.POST['site_url'], is_public = bool(request.POST['is_public']),  user = myus)
#         obj.save()
#         return render(request, 'home.html')


from password.forms import PasswordLogicForm
from password.views import GeneratePassword
from password.utils import generate_pwd 
from password.forms import PasswordForm
from password.models import Passwords



class HomeView(CreateView):
    # template_name = 'home.html'
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
                # print(pwd)        
                # form = PasswordForm(request.POST)
                context = { 'pwd':pwd}
                return render(request, 'home.html',context=context)

            context = context = {'form1':form1, 'form2': form2 }
            return render(request, 'home.html',context=context)

        else:
            # print("in form 2")
            if request.user.is_authenticated:
                mypwd = request.POST['pwd']
                myus = request.user
                obj = Passwords(password = mypwd, user = myus)
                obj.save()
                # return render(request, 'home.html')
                return redirect('password:view_pwd')
            return redirect('user_profile:login')

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
    fields = ['tags_name']
    success_url = reverse_lazy('user_profile:home')

    def get_success_url(self):
        return reverse_lazy('user_profile:home')

    def form_valid(self, form):
        ob = form.save(commit=False)
        ob.user = self.request.user
        return super().form_valid(ob)

# class TagsDetailView(DetailView):
#     model = Tags
#     template_name = ".html"
# )
        # context = {}
        # context['length'] =  request.POST.get('length')
        # context['upper'] =  request.POST.get('uppercase')
        # context['lower'] =  request.POST.get('lowercase')
        # context['number'] =  request.POST.get('numbers')
        # context['symbol'] =  request.POST.get('symbols')
        # context['extra'] =  request.POST.get('extra_symbols')
        # print(context)