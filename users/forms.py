from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
#from users.models import Profile
#from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username=forms.CharField(label='Login-ppp')
    status=forms.CharField(label='Status')
    middle_name = forms.CharField(label='Отчество',required=False)
    password1=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class":"form-input"}))
    password2=forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={"class":"form-input"}))

    class Meta:
        model = get_user_model()
        fields=['username','status', 'last_name','first_name', 'middle_name', 'email', 'gruppa', 'password1', 'password2']
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

# class UserProfileForm(UserChangeForm):
#     password = None
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']

# class UserImageForm(forms.ModelForm):
#     #user = forms.CharField(widget=forms.ChoiceField())
#     image = forms.FileField(label='avatar', required=False)
#     status=forms.CharField(label='Преподаватель или студент')
#     middle_name = forms.CharField(label='Отчество')
#     class Meta:
#         model = Profile
#         fields = ('user','image', 'status', 'middle_name')


class ProfileUserForm(forms.ModelForm):
    username=forms.CharField(label="Login",widget=forms.TextInput(attrs={'class':'form-input'}))
    email=forms.CharField(required=False, label="Email",widget=forms.TextInput(attrs={'class':'form-input'}))
    status = forms.CharField(disabled=True, label="Статус",widget=forms.TextInput(attrs={'class':'form-input'}))
    middle_name = forms.CharField(label='Отчество')
    gruppa = forms.CharField(disabled=True, label='Группа')
    #status_user = forms.CharField(disabled=True, label="Статус пользователя",widget=forms.TextInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields=['image','username','email','status','first_name','last_name', 'middle_name', 'gruppa']#, 'status_user']
        labels={
            'first_name':'Имя',
            'last_name':'Фамилия',
            'middle_name':'Отчество',
        }
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-input'}),
            'last_name':forms.TextInput(attrs={'class':'form-input'}),
            'middle_name':forms.TextInput(attrs={'class':'form-input'}),
            'gruppa':forms.TextInput(attrs={'class':'form-input'}),
        }



           