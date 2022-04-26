import imp
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from user_profile.models import Site

# Create your models here.
# TODO :catgories - one to one (accept NULL) ,description()
class Passwords(models.Model):

    class CategoryChoices(models.TextChoices):
        ENTERTAINMENT = 'ENT'
        LEARNING = 'LER'
        SHOPPING = 'SHO'

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    password = models.CharField(max_length=200, null=False)
    desciption = models.TextField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200)
    
    site = models.ForeignKey(Site,on_delete=models.CASCADE, null=True)

    category = models.CharField(max_length=300, choices=CategoryChoices.choices, null=True)

    def __str__(self):
        return self.email