from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Passwords
from .forms import PasswordForm, PasswordEditForm, PasswordAllFieldForm
from .utils import generate_pwd
from django.http import Http404

class GeneratePassword(CreateView):

    def get(self, request , *args, **kwargs):

        pwd = generate_pwd(8,True,True,True,True,False)
        form = PasswordForm(request.POST)
        context = { 'pwd':pwd ,"check":" "} 
        
        return render(request, 'home.html',context=context)
        
    
    def post(self, request, *args, **kwargs):
        print("this callledddd")
        if request.user.is_authenticated:   
            mypwd = request.POST['pwd']
            myus = request.user
            obj = Passwords(password = mypwd, user = myus)
            obj.save()
            
            # return render(request, 'home.html')
            return redirect('password:view_pwd')
            
        return redirect('user_profile:login')


# @login_required
# def view_password(request):
#     myuser = User.objects.get(username = request.user)
#     pwd = Passwords.objects.filter(user = myuser)
#     context = {'passwords' : pwd}
#     return render(request, 'password/view_password.html', context= context)


#---View for All Password showing
class PasswordView(LoginRequiredMixin, ListView):
    model = Passwords
    context_object_name = 'passwords'
    template_name = 'password/view_password.html'
    login_url = 'user_profile:login'

    def get_queryset(self):
        myuser = User.objects.get(username = self.request.user)
        # import pdb; pdb.set_trace()
        if self.kwargs.get('tag',None):
            queryset = Passwords.objects.filter(user = myuser) .order_by('tag_id')
        else:
            queryset = Passwords.objects.filter(user = myuser) 
        return queryset


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(redirect_field_name='next', login_url=reverse_lazy('user_profile:login')), name='dispatch')
class EditPassword(SuccessMessageMixin, UpdateView):
    template_name = 'password/edit_password.html'
    # form_class = PasswordAllFieldForm
    form_class = PasswordEditForm
    success_url = reverse_lazy('password:view_pwd')

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.email = self.request.user.email
    #     return super().get(request, *args, **kwargs)

    def get_success_message(self, cleaned_data):
        return "Password is Edited successfully."

    def get_object(self):
        id_ = self.kwargs.get("id")
        p = Passwords.objects.get(id = id_)
        if not p.email:
            p.email = self.request.user.email
            p.save()
        if p.user == self.request.user:
            return get_object_or_404(Passwords, id=id_ )
        else:
            raise Http404("It seems you are talented to person to come this far, but you can't view Unauthorised Detail. Sorry, Apply for Simform Solutions.")


class PasswordDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Passwords
    template_name = "password/delete_password.html"
    success_url = reverse_lazy('password:view_pwd')
    login_url = 'user_profile:login'
    
    def get_success_message(self, cleaned_data):
        return "Password is deleted successfully."

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        if self.object.user == request.user:
            return self.render_to_response(context)
        raise Http404("It seems you are talented to person to come this far, but you can't Delete Unauthorised Detail. Sorry, Apply for Simform Solutions.")

    # def delete(self, request, *args, **kwargs):
    #     messages.success(self.request, self.success_message)
    #     return super(PasswordDeleteView, self).delete(request, *args, **kwargs)
        


class PasswordCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Passwords
    template_name = "password/add_pwd.html"
    field = "__all__"
    form_class = PasswordAllFieldForm
    login_url = 'user_profile:login'
    success_url = reverse_lazy('password:view_pwd')

    def get_success_message(self, cleaned_data):
        return "Password Created Successfully."

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PasswordCreateView, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.pk
        return kwargs




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
