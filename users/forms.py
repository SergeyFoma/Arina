from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    username=forms.CharField(label='Login')
    password=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class":"form-input"}))
    password2=forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={"class":"form-input"}))

    class Meta:
        model = get_user_model()
        fields=['username', 'last_name','first_name', 'email', 'password', 'password2']
        labels={
            'email':'Email',
            'first_name':'Имя',
            'last_name':'Фамилия',
        }

class LoginForm(AuthenticationForm):
    username=forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class":"form-input"}))
    password=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class":"form-input"}))
    class Meta:
        model=get_user_model()
        fields=['username', 'password']
