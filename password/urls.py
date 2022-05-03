from django.urls import path
from . import views

urlpatterns = [
    path('passwords/', views.view_password, name="view_password"),
    path('edit_pwd/<int:id>', views.EditPassword.as_view(), name="edit_pwd"),
    path('generate_pwd/', views.GeneratePassword.as_view(), name="generate_pwd"),
    path('delete_password/<int:pk>', views.PasswordDeleteView.as_view(), name="delete_pwd"),
]