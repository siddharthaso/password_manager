from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('generate_pwd/', views.generate_pwd, name="generate_pwd"),
]