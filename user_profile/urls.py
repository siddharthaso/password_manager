from django.urls import path
from . import views

app_name = 'user_profile'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name="profile"),

    path('login/',views.LoginFormView.as_view(), name = 'login'),
    path('logout/',views.LogoutView.as_view(), name = 'logout'),

    path('add_site/',views.CreateSiteView.as_view(), name = 'add_site'),
    path('create_tag/',views.TagsCreateView.as_view(), name = 'create_tag'),
]