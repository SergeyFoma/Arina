from django.urls import path
from . import views

from django.contrib.auth import views as auth_views #для смены пароля

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('profile/', views.profile, name='profile'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name="password_reset_complete"),
]