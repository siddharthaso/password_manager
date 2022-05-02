from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from password.models import Passwords

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from password.forms import PasswordForm

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
            
        return render(request, 'general/generated_pwd.html',context=context)
        
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            mypwd = request.POST['pwd']
            myus = request.user
            obj = Passwords(password = mypwd, user = myus)
            obj.save()
        else:
            return redirect('login')
        
        return render(request, 'home.html')