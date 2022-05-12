from django.db import models
from django.contrib.auth.models import User
from user_profile.models import Site, Tags


class Passwords(models.Model):

    class CategoryChoices(models.TextChoices):
        ENTERTAINMENT = 'ENT'
        LEARNING = 'LER'
        SHOPPING = 'SHO'
        PAYMENT = "PAY"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'passwords')

    password = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200)
    
    site = models.ForeignKey(Site,on_delete=models.CASCADE, null=True, blank=True, related_name = 'passwords')

    category = models.CharField(max_length=300, choices=CategoryChoices.choices, null=True)

    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, null= True, blank =True, related_name = 'passwords')

    def __str__(self):
        return self.password