from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail

@shared_task(bind = True)
def sending_mail(self,subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)
    print("sended mail because of password of email i can't send with heroku")