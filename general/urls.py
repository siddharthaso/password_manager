from django.urls import path
from . import views
from .views import GeneratePassword

urlpatterns = [
    path('generate_pwd/', GeneratePassword.as_view(), name="generate_pwd"),
]