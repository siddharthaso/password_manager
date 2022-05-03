from django.urls import path
from . import views
from .views import CreateSiteView, LoginFormView, LogoutView
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name="profile"),

    path('login/',LoginFormView.as_view(), name = 'login'),
    path('logout/',LogoutView.as_view(), name = 'logout'),

    path('add-site/',CreateSiteView.as_view(), name = 'add_site'),
]