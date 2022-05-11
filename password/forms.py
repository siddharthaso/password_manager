from email.policy import default
from lib2to3.pygram import Symbols
from django import forms
from .models import Passwords
from django.core.exceptions import ValidationError
from django.core import validators

class PasswordLogicForm(forms.Form):

    length = forms.IntegerField(label='Length of the Password', required=False) #validators=[validators.MaxLengthValidator(5)]
    uppercase = forms.BooleanField(label='Include Uppercase ( e.g. ABCDEFGH )', required=False)
    lowercase = forms.BooleanField(label='Include Lowercase( e.g. abcdefgh )', required=False)
    numbers = forms.BooleanField(label='Include Number ( e.g. 123456 )', required=False)
    symbols = forms.BooleanField(label='Include Symbols ( e.g. @#$% )', required=False)
    extra_symbols = forms.BooleanField(label='Include Extra Symbols [ e.g. =:?./|~>*()< ]', required=False)


    def clean(self):
        print("called")
        # print(self.uppercase)
        cleaned_data = super(PasswordLogicForm, self).clean()
        
        #lambda map filter , .item of dict
        print(cleaned_data)        
        s = cleaned_data['uppercase']+cleaned_data['lowercase']+cleaned_data['numbers']+cleaned_data['symbols']+cleaned_data['extra_symbols']
        # from functools import reduce
        # s1 = reduce(lambda a,b:a+b ,list(cleaned_data.values())[1:])
        
        if cleaned_data.get('length') <= 5:
            raise ValidationError("Minimum length 5 of Password is Required")
        elif(s < 3):                               
            raise ValidationError("Minimum 3 Choice is necessary to make stronger password")

class PasswordForm(forms.ModelForm):
    # model = Passwords
    # Uppercase = forms.BooleanField()
    # Lowercase = forms.BooleanField()
    # Numbers = forms.BooleanField()
    # Symbols = forms.BooleanField()
    # length = forms.IntegerField()

    # extra_field_count = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model= Passwords
        fields = ['password']
        # ,'Uppercase','Lowercase', 'Numbers', 'Symbols', 'length']

class PasswordAllFieldForm(forms.ModelForm):
    # model = Passwords
    class Meta:
        model= Passwords
        fields = '__all__'

# class PasswordForm(forms.ModelForm):
#     class Meta:
#         model = Passwords
#         exclude = ('user',)