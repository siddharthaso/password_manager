from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/',views.register,name="register"),

    path('login/',authentication_views.LoginView.as_view(template_name = 'user_profile/login.html'), name = 'login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name = 'user_profile/logout.html'), name = 'logout'),
]