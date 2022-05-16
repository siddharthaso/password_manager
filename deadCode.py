# ---Login view---
# from django.contrib import messages
# from django.contrib.auth.views import LoginView, LogoutView
# class LoginFormView(SuccessMessageMixin, LoginView):
#     template_name = 'user_profile/login.html'

#     def get_success_message(self, cleaned_data):
#         return f"You are now successfully logged in as {self.request.user.username.capitalize()}."


#------Logout view-----------
# from django.contrib.auth.views import LogoutView
# class LogoutFormView(LogoutView):
#     def get_next_page(self):
#         next_page = super(LogoutFormView, self).get_next_page()
#         messages.add_message(
#             self.request, messages.SUCCESS,
#             'You successfully log out!'
#         )
#         return next_page


#-----Register/Sign-up-----
# class RegisterView(SuccessMessageMixin, CreateView):
#     form_class =  RegisterForm
#     template_name = "user_profile/register.html"
#     success_url = reverse_lazy('user_profile:home')
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             username = self.request.user.username
#             # messages.success(self.request, f'Welcome {username}, your account is created ')
#             success_message = f'Welcome {username.capitalize()}, your account is created '
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#     def form_valid(self, form):
#         ob = form.save(commit=False)
#         return super().form_valid(ob)


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


#---View for Viewing All Password
# @login_required
# def view_password(request):
#     myuser = User.objects.get(username = request.user)
#     pwd = Passwords.objects.filter(user = myuser)
#     context = {'passwords' : pwd}
#     return render(request, 'password/view_password.html', context= context)


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


# generate_pwd.html-------------------
# {%extends 'base.html'%}


# {% block content%}
# <div class="main-content col-6 justify-content-center text-center" style="margin-bottom: 300px;">
#     <div id="password-generator">
#         <!-- password geenrator -->
#         <div id = "password-generator">
#             <h1 >Generate Your Password here</h1>
#             <a href="{% url 'password:generate_pwd'%}"><h2 id="th">Click here to Generate</h2></a>
#         </div>
        
#         <h1>Generated password: </h1>
#         <h2>{{pwd}} &nbsp &nbsp <i class="fa fa-copy" aria-hidden="true"></i></h2>
#         <br>
#         Generated Password: &nbsp {{pwd}} &nbsp &nbsp <i class="fa fa-copy" aria-hidden="true"></i>

#         <form method="POST" action="">
#             {% csrf_token %}
#             <!-- {{ form.password.as_hidden }} -->
#             <input type="hidden" name="pwd" value="{{pwd}}">
#             <br>

#             {% if user.is_authenticated %}
#                 <button class="btn btn-primary" type ="submit">Save Password</button>
#             {% else %}
#                 To Save Password Click on <a href="{% url 'user_profile:login'%}">Login</a>
#             {% endif %}
#         </form>
        
#     </div>    
# </div>

# {% endblock content%}   

# PROFILE.HTML--------------------
# <!-- body{padding-top:30px;} -->

# <!-- .glyphicon { margin-bottom: 10px;margin-right: 10px;}
# style="margin-bottom: 10px;margin-right: 10px;"
# small {
# display: block;
# line-height: 1.428571429;
# color: #999;
# } -->

# {% comment %} {% for x in data %} {% endcomment %}
# {% comment %} 
# <h1>Username : {{ user.username }}</h1>
# <h1>Email addresss : {{ user.email }}</h1>
# <h1>Locations : {{ profile.location }}</h1>
# {{ profile.profile_picture.image.url }}
# <h1>Profile picture : </h1><img src="{{ profile.profile_picture.image.url }}"> {% endcomment %}

# {% comment %} {% endfor %} {% endcomment %}

