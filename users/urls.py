from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth import views as auth_views #для смены пароля

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('profile/', views.profile, name='profile'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),

    path('password_reset_form/', 
         auth_views.PasswordResetView.as_view(
               template_name="users/password_reset_form.html",
               email_template_name="users/password_reset_email.html",
               success_url=reverse_lazy("users:password_reset_done"),
          ),
         name="password_reset_form"),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name="password_reset_done"),

    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="users/password_reset_confirm.html",
             success_url=reverse_lazy("users:password_reset_complete"),
             ),
         name="password_reset_confirm"),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name="password_reset_complete"),
]