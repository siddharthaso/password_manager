from django.urls import path
from . import views

urlpatterns = [
    path('passwords/', views.view_passwords, name="view-passwords"),
    path('edit_pwd/<int:id>', views.EditPassword.as_view(), name="edit_pwd"),
]