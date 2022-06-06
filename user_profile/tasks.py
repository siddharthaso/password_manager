from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail

@shared_task(bind = True)
def sending_mail(self,subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)

import datetime
from django.http import FileResponse
from django.contrib.auth.models import User
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import json
from django.conf import settings

@shared_task(bind = True)
def download_user(self):
    u = User.objects.all()

    buf = io.BytesIO()
    c = canvas.Canvas(settings.MEDIA_ROOT + 'pdf/file_name.pdf')
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont('Helvetica',14)
    for i in u:
        textob.textLines(str(i))
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return json.dumps(FileResponse(buf,as_attachment=True, filename='user_list.pdf'))