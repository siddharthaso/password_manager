from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from password.models import Passwords


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 

# @receiver(post_save, sender = Passwords)
# def save_email_address(sender, instnace, created, **kwargs):
#         pwd = Passwords.objects.get(instnace=instnace)
#         print(pwd)
#         # instnace.save()