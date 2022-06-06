import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','password_manager.settings')
app = Celery('password_manager')

app.config_from_object('password_manager.settings', namespace="CELERY")

app.conf.beat_schedule = {
    'send-mail-once-in-a-day':{
    'task':'user_profile.tasks.download_user',
    'schedule': crontab(hour=12 , minute=30)
 }
}

app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')