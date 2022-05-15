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
