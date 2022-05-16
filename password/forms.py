from django import forms
from django.core.exceptions import ValidationError
from user_profile.models import Tags, Site
from .models import Passwords

#For Home page password creation form and its validation
class PasswordLogicForm(forms.Form):

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
        s = sum(d.values())

        # s = cleaned_data['uppercase']+cleaned_data['lowercase']+cleaned_data['numbers']+cleaned_data['symbols']+cleaned_data['extra_symbols']
        # from functools import reduce
        # s1 = reduce(lambda a,b:a+b ,list(cleaned_data.values())[2:])

        if leng:
            if leng <= 5 and s < 3:
                raise ValidationError("Minimum Length 6 and Choice 3 is Required")
            elif leng <= 5:
                raise ValidationError("Minimum Length 6 of Password is Required")
            elif(s < 3):                               
                raise ValidationError("Minimum 3 Choice is Necessary to make Stronger Password")
        else:
            raise ValidationError("Length is required")

#Form for Creating Password Manually
class PasswordAllFieldForm(forms.ModelForm):
    class Meta:
        model= Passwords
        fields = '__all__'

    def __init__(self, *args, user_id=None, **kwargs):
        # self.user = kwargs.pop('user',None)
        super(PasswordAllFieldForm, self).__init__(*args, **kwargs)

        if self.instance:
            self.fields['tag'].queryset = Tags.objects.filter(user=user_id)
            self.fields['site'].queryset = Site.objects.filter(user=user_id)

#Form for storing Only password after generating it
class PasswordForm(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = ['password']
        # exclude = ('user',)

#Form for Editing existing password of particular user
class PasswordEditForm(forms.ModelForm): 

    class Meta:
        model= Passwords
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PasswordEditForm, self).__init__(*args, **kwargs)

        if self.instance:
            self.fields['tag'].queryset = Tags.objects.filter(user=self.instance.user)
            self.fields['site'].queryset = Site.objects.filter(user=self.instance.user)
    
    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user',None)
    #     super(PasswordEditForm, self).__init__(*args, **kwargs)

    #     if self.instance:
    #         self.fields['tag'].queryset = Tags.objects.filter(user=self.user)
    #         self.fields['site'].queryset = Site.objects.filter(user=self.user)