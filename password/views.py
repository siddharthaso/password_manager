from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Passwords
from django.contrib.auth.models import User
from .forms import PasswordForm, PasswordAllFieldForm
from django.views.generic import CreateView,UpdateView

# Create your views here.

@login_required
def save_pwd(request):
    # if request.method == 'POST':
    #     form = PasswordForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'{username}, You have stored the password successfully.')
    #         return redirect('home')
    # else:
        
    #     form = PasswordForm()
    # p = Passwords.objects.create(user = )

    return render(request, 'password/save_password.html')#,{'form':form})

@login_required
def view_passwords(request):
    myuser = User.objects.get(username = request.user)
    print(myuser)
    pwd = Passwords.objects.filter(user = myuser)
    print(pwd)
    context = {'user' : myuser, 'passwords' : pwd}
    return render(request, 'password/view_passwords.html', context= context)

# @login_required
# def edit_password(request, id):
#     PasswordAllFieldForm()
#     pwd = Passwords.objects.get(id = id)
#     context = {'user' : myuser, 'passwords' : pwd}
#     return render(request, 'password/view_passwords.html', context= context)

class EditPassword(UpdateView):

    def get(self, request , *args, **kwargs):   
        pwd = Passwords.objects.get(id = self.kwargs['id'])     
        form = PasswordAllFieldForm(request.POST, instance=pwd)
        context = {'form':form}
            
        return render(request, 'general/edit_password.html',context=context)
        
    
    def post(self, request, *args, **kwargs):
        mypwd = request.POST
        mypwd.save()
        return render(request, 'home.html')