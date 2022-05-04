from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name = 'profile')
    profile_picture = models.ImageField(default = 'profile_pic.png', upload_to = '')
    location = models.CharField(max_length=140)

    def __str__(self) -> str:
        return self.user.username


class Site(models.Model):

    site_name = models.CharField(max_length=300)
    site_url = models.CharField(max_length=300, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name = 'site')

    def __str__(self) -> str:
        return self.site_name


# TODO :color for different tags , passwords- one to many, abbrevation (short form)-> require slug
class Tags(models.Model):
    
    tags_name = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name = 'tags')

    def __str__(self) -> str:
        return self.tags_name