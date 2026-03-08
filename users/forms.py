from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from users.models import Profile
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username=forms.CharField(label='Login-ppp')
    password1=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class":"form-input"}))
    password2=forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={"class":"form-input"}))

    class Meta:
        model = get_user_model()
        fields=['username', 'last_name','first_name', 'email', 'password1', 'password2']
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

class UserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserImageForm(forms.ModelForm):
    #user = forms.CharField(widget=forms.ChoiceField())
    image = forms.FileField(label='avatar', required=False)
    class Meta:
        model = Profile
        fields = ('user','image',)


