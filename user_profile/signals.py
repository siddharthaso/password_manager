from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from password.models import Passwords
from django.core.mail import send_mail
from django.conf import settings

# import smtplib, ssl
# port = 465  # For SSL
# password = input("Type your password and press enter: ")

# # Create a secure SSL context
# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("my@gmail.com", password)
    # TODO: Send email here



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        print(kwargs)

        subject = 'Congratulation on sign up'
        # import pdb; pdb.set_trace()
        # user
        message = f'Hi {instance.username}, thank you for Using our Website.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email,]
        send_mail(subject, message, email_from, recipient_list)

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