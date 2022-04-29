from django.urls import path
from . import views

urlpatterns = [
    path('save_pwd/', views.save_pwd, name="save-pwd"),
]