from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

app_name = 'user_profile'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),

    # path('register/',views.register,name="register"),
    path('register/',views.RegisterView.as_view(),name="register"),
    path('profile/',views.profile,name="profile"),

    path('login/', LoginView.as_view(template_name = "user_profile/login.html"), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = "user_profile/logout.html"), name = 'logout'),

    path('add_site/',views.CreateSiteView.as_view(), name = 'add_site'),
    path('create_tag/',views.TagsCreateView.as_view(), name = 'create_tag'),
]