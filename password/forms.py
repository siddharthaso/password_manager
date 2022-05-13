from django import forms
from .models import Passwords
from django.core.exceptions import ValidationError
# from django.core import validators

class PasswordLogicForm(forms.Form):
    form1 = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    length = forms.IntegerField(label='Length of the Password', required=False) #validators=[validators.MaxLengthValidator(5)]
    uppercase = forms.BooleanField(label='Include Uppercase ( e.g. ABCDEFGH )', required=False)
    lowercase = forms.BooleanField(label='Include Lowercase( e.g. abcdefgh )', required=False)
    numbers = forms.BooleanField(label='Include Number ( e.g. 123456 )', required=False)
    symbols = forms.BooleanField(label='Include Symbols ( e.g. @#$% )', required=False)
    extra_symbols = forms.BooleanField(label='Include Extra Symbols [ e.g. =:?./|~>*()< ]', required=False)

    def clean(self):
        cleaned_data = super(PasswordLogicForm, self).clean()
        
        d = dict(cleaned_data)
        leng = d.pop('length') or 0

        s = cleaned_data['uppercase']+cleaned_data['lowercase']+cleaned_data['numbers']+cleaned_data['symbols']+cleaned_data['extra_symbols']
        
        from functools import reduce
        s1 = reduce(lambda a,b:a+b ,list(cleaned_data.values())[2:])

        if leng:
            if leng <= 5 and s < 3:
                raise ValidationError("Minimum Length 6 and Choice 3 is Required")
            elif leng <= 5:
                raise ValidationError("Minimum Length 6 of Password is Required")
            elif(s < 3):                               
                raise ValidationError("Minimum 3 Choice is Necessary to make Stronger Password")
        else:
            raise ValidationError("Length is required")


# class PasswordForm(forms.Form):
#     password = forms.CharField(max_length=200, required=True)
# class PasswordForm(forms.ModelForm):
#     class Meta:
#         model= Passwords
#         fields = ['password','user']
#         # ,'Uppercase','Lowercase', 'Numbers', 'Symbols', 'length']

class PasswordAllFieldForm(forms.ModelForm):
    # model = Passwords
    class Meta:
        model= Passwords
        fields = '__all__'

class PasswordForm(forms.ModelForm):
    form2 = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Passwords
        fields = ['password']
        # exclude = ('user',)