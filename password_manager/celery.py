import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','password_manager.settings')
app = Celery('password_manager')

app.config_from_object('password_manager.settings', namespace="CELERY")

# app.conf.beat_schedule = {

# }

app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')