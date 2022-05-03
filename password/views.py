from urllib import request
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Passwords
from django.contrib.auth.models import User
from .forms import PasswordForm, PasswordAllFieldForm
from django.views.generic import CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import PasswordForm

# Create your views here.

class GeneratePassword(CreateView):

    def get(self, request , *args, **kwargs):
        
        import random
        import array

        MAX_LEN = 12

        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)

        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)

            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)

        password = ""
        for x in temp_pass_list:
            password = password + x
                
        # if request.method == 'POST':
        #     form = PasswordForm(request.POST)
        #     if form.is_valid():
        #         form.save()
        #         return redirect('home')
        # else:
            
        #     form = PasswordForm()

        form = PasswordForm(request.POST)
        context = { 'pwd':password, 'form':form}
        print(password)
            
        return render(request, 'password/generate_pwd.html',context=context)
        
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            mypwd = request.POST['pwd']
            myus = request.user
            obj = Passwords(password = mypwd, user = myus)
            obj.save()
        else:
            return redirect('login')
        
        return render(request, 'home.html')


@login_required
def view_password(request):
    myuser = User.objects.get(username = request.user)
    pwd = Passwords.objects.filter(user = myuser)
    context = {'user' : myuser, 'passwords' : pwd}
    return render(request, 'password/view_password.html', context= context)


class EditPassword(UpdateView):
    template_name = 'password/edit_password.html'
    form_class = PasswordAllFieldForm
    
    # success_url = '/passwords/'
    success_url = reverse_lazy('view_password')
    
    # /home/siddharthasodariya/Django/password_manager/profile_pictures/edit_pwd/passwords” does not exist
    # success_url = 'passwords'

    def get_object(self):
        id_ = self.kwargs.get("id")
        p = Passwords.objects.get(id = id_)
        p.email = self.request.user.email
        p.save()
        return get_object_or_404(Passwords, id=id_)

    
    # def get(self, request , *args, **kwargs):   
    #     pwd = Passwords.objects.get(id = self.kwargs['id'])
    #     form = PasswordAllFieldForm(request.POST or None, instance=pwd)
    #     print(pwd.user.email)
    #     context = {'form':form}
    #     return render(request,template_name,context=context)
        
    # def post(self, request, *args, **kwargs):
    #     data = request.POST    
    #     print(mypwd)
    #     mypwd.save()
    #     return render(request, 'home.html')
    #     obj = Passwords.get_or_create(site_name =request.POST['site_name'], site_url = request.POST['site_url'], is_public = bool(request.POST['is_public']),  user = myus)
    #     'user'= request.user, 'password': ['IKEc:Am2v#d~'], 'description': ['This is for twitter'], 'email': ['siddharth@gmail.com'], 'site': ['2'], 'category': ['ENT']}>
    #     obj.save()
        
    #     return render(request, 'home.html')

class PasswordDeleteView(DeleteView):
    model = Passwords
    template_name = "password/delete_password.html"
    success_url = reverse_lazy('view_password')

    # def get_success_url(self):
    #     return reverse('view_password', kwargs={'id': self.kwargs.get("id")})
    #     # kwargs={'pk': self.object.k})

    # success_message = f'Password {Passwords.objects.get(id = self.kwargs.get("id"))} was deleted successfully.'
    success_message = "Password was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PasswordDeleteView, self).delete(request, *args, **kwargs)