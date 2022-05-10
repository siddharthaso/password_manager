from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView, DeleteView, ListView
from django.contrib.auth.models import User

from .models import Passwords
from .forms import PasswordForm, PasswordAllFieldForm
from .forms import PasswordForm
from .utils import generate_pwd

class GeneratePassword(CreateView):

    def get(self, request , *args, **kwargs):
        
        pwd = generate_pwd(8,True,True,True,True,False)
        form = PasswordForm(request.POST)
        context = { 'pwd':'password', 'form':form}
            
        return render(request, 'password/generate_pwd.html',context=context)
        
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            mypwd = request.POST['pwd']
            myus = request.user
            obj = Passwords(password = mypwd, user = myus)
            obj.save()
            
            return render(request, 'home.html')
            
        return redirect('user_profile:login')


# @login_required
# def view_password(request):
#     myuser = User.objects.get(username = request.user)
#     pwd = Passwords.objects.filter(user = myuser)
#     context = {'passwords' : pwd}
#     return render(request, 'password/view_password.html', context= context)

class PasswordView(ListView):
    model = Passwords
    context_object_name = 'passwords'
    
    template_name = 'password/view_password.html'

    def get_queryset(self):
        myuser = User.objects.get(username = self.request.user)
        queryset = Passwords.objects.filter(user = myuser) 
        return queryset


class EditPassword(UpdateView):
    template_name = 'password/edit_password.html'
    form_class = PasswordAllFieldForm
    
    # success_url = '/passwords/'
    success_url = reverse_lazy('password:view_password')

    def get_object(self):
        id_ = self.kwargs.get("id")
        p = Passwords.objects.get(id = id_)
        p.email = self.request.user.email
        p.save()
        return get_object_or_404(Passwords, id=id_)


class PasswordDeleteView(DeleteView):
    model = Passwords
    template_name = "password/delete_password.html"
    success_url = reverse_lazy('password:view_password')

    # success_message = f'Password {Passwords.objects.get(id = self.kwargs.get("id"))} was deleted successfully.'
    success_message = "Password was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PasswordDeleteView, self).delete(request, *args, **kwargs)
        

class PasswordCreateView(CreateView):
    model = Passwords
    template_name = "password/add_pwd.html"
    field = "__all__"
    form_class = PasswordAllFieldForm
    success_url = reverse_lazy('password:view_password')




# class EditPassword(UpdateView):
    
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
