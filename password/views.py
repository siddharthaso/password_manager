from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView, DeleteView, ListView
from django.shortcuts import render,redirect, get_object_or_404
from django.http import Http404

from .models import Passwords
from .forms import PasswordEditForm, PasswordAllFieldForm
from .utils import generate_pwd

#Generate Password by Default Configuration of Choices
class GeneratePassword(CreateView):

    def get(self, request , *args, **kwargs):

        pwd = generate_pwd(8,True,True,True,True,False)
        context = { 'pwd':pwd ,"check":" "} 
        
        return render(request, 'home.html',context=context)
        
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:   
            mypwd = request.POST['pwd']
            myus = request.user
            obj = Passwords(password = mypwd, user = myus)
            obj.save()
            
            return redirect('password:view_pwd')
            
        return redirect('user_profile:login')

#---View for Viewing All Password and also for sorted password
class PasswordView(LoginRequiredMixin, ListView):
    model = Passwords
    context_object_name = 'passwords'
    template_name = 'password/view_password.html'
    login_url = 'user_profile:login'

    def get_queryset(self):
        myuser = User.objects.get(username = self.request.user)
        if self.kwargs.get('tag',None):
            queryset = Passwords.objects.filter(user = myuser) .order_by('tag_id')
        else:
            queryset = Passwords.objects.filter(user = myuser) 
        return queryset


#View for editing Password
@method_decorator(login_required(redirect_field_name='next', login_url=reverse_lazy('user_profile:login')), name='dispatch')
class EditPassword(SuccessMessageMixin, UpdateView):

    template_name = 'password/edit_password.html'
    form_class = PasswordEditForm
    success_url = reverse_lazy('password:view_pwd')

    def get_success_message(self, cleaned_data):
        return "Password Updated successfully."

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

#View for deleting password
class PasswordDeleteView(LoginRequiredMixin, DeleteView):
    model = Passwords
    template_name = "password/delete_password.html"
    success_url = reverse_lazy('password:view_pwd')
    login_url = 'user_profile:login'
    success_message = "Password deleted successfully."

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        if self.object.user == request.user:
            return self.render_to_response(context)
        raise Http404("It seems you are talented to person to come this far, but you can't Delete Unauthorised Detail. Sorry, Apply for Simform Solutions.")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PasswordDeleteView, self).delete(request, *args, **kwargs)
        

#View for creating password manually
class PasswordCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Passwords
    template_name = "password/add_pwd.html"
    field = "__all__"
    form_class = PasswordAllFieldForm
    login_url = 'user_profile:login'
    success_url = reverse_lazy('password:view_pwd')

    def get_success_message(self, cleaned_data):
        return "Password Created Successfully."

    #To pass current logged  in user detail to Form to filter Tags and site fields
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PasswordCreateView, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.pk
        return kwargs