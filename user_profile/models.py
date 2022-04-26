from django.db import models
from django.contrib.auth.models import User



# TODO : crating model for site, passwords-one to many 
#user_profile -one to many, is_public =True , categories- one to many (accept NUll)
class Site(models.Model):
    site_name = models.CharField(max_length=300)
    site_url = models.CharField(max_length=300, null=True, blank=True)
    is_public = models.BooleanField(default=True)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'profile_pictures', blank = True)
    location = models.CharField(max_length=140)
    site = models.ForeignKey(Site,on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.user.username


# TODO :personalization category, color for different tags
#user_profile - one to many, passwords- one to many
# abbrevation (short form)-> require slug
class Tags(models.Model):
    class TagsChoices(models.TextChoices):
        HOME = 'HM'
        OFFICE = 'OF'   

    tags_name = models.CharField(max_length=300,choices = TagsChoices.choices,default = TagsChoices.OFFICE)