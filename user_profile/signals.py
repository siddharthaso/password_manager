from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from user_profile.tasks import sending_mail
from django.conf import settings

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        subject = 'Welecome to Password Manager'
        # message = f'Hi {instance.username}, thank you for registering in Password manager.'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [instance.email,]
        # sending_mail.delay(subject, message, email_from, recipient_list)

@receiver(post_save, sender=User)   
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 

@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, f"You are now successfully logged in as {request.user.username.capitalize()}.")

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'You have Successfully logged out.')