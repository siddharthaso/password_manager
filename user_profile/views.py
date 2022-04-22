from django.shortcuts import render
# from .forms import loginForm
# from .forms import signupForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def generate_pwd(request):

    return render(request, 'output.html')

# Create your views here.
def home(request):
    return render(request , 'home.html')    


# Create your views here.
def login(request):
    # if request.method == 'POST':
    #     form = loginForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     context = {'form':form}
    # else:
    #     form = loginForm()
    #     print(form)
    # return render(request, 'login.html', {'form':form})
    pass

# from django import forms
# class LoginForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)

# Create your views here.

def signup(request):
    # if request.method == 'POST':
    #     # print(request)
    #     form = signupForm(request.POST)
    #     if form.is_valid():
    #         # p1 = form.cleaned_data.get('password1')
    #         # p2 = form.cleaned_data.get('password2')
    #         # if p1 == p2:
    #         #     print("hh")
    #         #     form.save()
    #         # else:
    #         #     print("Invalid")
    #         form.save()
    #     else:
    #         print(messages.error)
    #     # context = {'form':form}
    # else:
    #     form = signupForm()
    #     print(form)
    # return render(request , 'sign-up.html', {'form':form})    
    pass

def generate_pwd(request):
    # import secrets
    # import string

    # # secure random string
    # secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(8)))
    # print(secure_str)
    # # Output QQkABLyK

    # # secure password
    # password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
    # # print(password)
    # # output 4x]>@;4)

    import random
    import array

    # maximum length of password needed
    # this can be changed to suit your password length
    MAX_LEN = 12

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
            password = password + x
            
    # print out password
    print(password)
    context = { 'pwd':password}
    return render(request, template_name='generated_pwd.html', context=context)