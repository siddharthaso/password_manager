from django.urls import path
from . import views

app_name = 'password'

#http://127.0.0.1:8000/
urlpatterns = [
    
    # path('passwords/', views.view_password, name="view_pwd"),
    path('passwords/', views.PasswordView.as_view(), name="view_pwd"),
    path('view_sorted_pwd/<str:tag>', views.PasswordView.as_view(), name="view_sorted_pwd"),

    path('edit_pwd/<int:id>', views.EditPassword.as_view(), name="edit_pwd"),
    path('generate_pwd/', views.GeneratePassword.as_view(), name="generate_pwd"),
    path('delete_password/<int:pk>', views.PasswordDeleteView.as_view(), name="delete_pwd"),
    path('add_password/', views.PasswordCreateView.as_view(), name="add_pwd"),
]