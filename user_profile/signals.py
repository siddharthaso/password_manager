from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from password.models import Passwords
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        print(kwargs)

        send_mail(
            'Subject here',
            'Here is the message.',
            'tracy.rippin29@gmail.com',
            [instance.email],
            fail_silently=False,
            auth_user= 'tracy.rippin29@gmail.com',
            auth_password='@#$123sddd'
        )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 

# @receiver(post_save, sender = Passwords)
# def save_email_address(sender, instnace, created, **kwargs):
#         pwd = Passwords.objects.get(instnace=instnace)
#         print(pwd)
#         # instnace.save()

@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, f"You are now successfully logged in as {request.user.username.capitalize()}.")

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'You have Successfully logged out.')