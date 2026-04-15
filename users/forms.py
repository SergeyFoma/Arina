from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
#from users.models import Profile
#from django.contrib.auth.models import User

CHOICES = [
    ('-----','-----'),
    ('student', 'Студент'),
    ('teacher', 'Преподаватель'),
    ('admin', 'Администратор'),
]
class RegisterForm(UserCreationForm):
    username=forms.CharField(label='Login-ppp')
    status=forms.ChoiceField(label='Выберите свой вариант', choices = CHOICES, widget = forms.Select(attrs={'class':'form-input'}),required=True)
    middle_name = forms.CharField(label='Отчество',required=False)
    gruppa = forms.CharField(label='Группа', widget=forms.TextInput(attrs={'class':"form-input"}), required=True)
    password1=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class":"form-input"}))
    password2=forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={"class":"form-input"}))
    #number = forms.CharField(label = 'Верификационный номер')

    class Meta:
        model = get_user_model()
        fields=['username','status', 'last_name','first_name', 'middle_name', 'email', 'gruppa',  'password1', 'password2']
        labels={
            'email':'Email',
            'first_name':'Имя',
            'last_name':'Фамилия',
        }


from .models import Group, CustomUser

class RoleSelectionForm(forms.Form):
    ROLE_CHOICES = [
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

group_num=Group.objects.all()
GROUP_CHOICES=[]
for i in group_num:
    GROUP_CHOICES.append((i,i))
class StudentRegistrationForm(forms.ModelForm):
    group_number = forms.ChoiceField( label="Номер группы", choices=GROUP_CHOICES)
    #group_number = forms.CharField(label='numb')
    group_as_student = forms.ChoiceField( label="Номер группы", choices=GROUP_CHOICES)
    #status=forms.ChoiceField(label='Выберите свой вариант', choices = CHOICES, widget = forms.Select(attrs={'class':'form-input'}),required=True)
    status = forms.CharField(initial = 'Студент')
    password1=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class":"form-input"}))
    password2=forms.CharField(label='Повтор пароля' , widget=forms.PasswordInput(attrs={"class":"form-input"}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'group_number', 'status']

class TeacherRegistrationForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Группы"
    )
    status = forms.CharField(initial = 'Преподаватель')
    password2=forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={"class":"form-input"}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password','password2', 'groups', 'status']



   

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
    #status = forms.CharField(disabled=True, label="Статус",widget=forms.TextInput(attrs={'class':'form-input'}))
    middle_name = forms.CharField(label='Отчество')
    #gruppa = forms.CharField(disabled=True, label='Группа')
    #status_user = forms.CharField(disabled=True, label="Статус пользователя",widget=forms.TextInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()        
        fields=['image','username','email','first_name', 'middle_name','last_name','group_as_student','groups_as_teacher']#, 'status_user']
        labels={
            'first_name':'Имя',
            'last_name':'Фамилия',
            'middle_name':'Отчество',
            'group_as_student':'Студент'
        }
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-input'}),
            'last_name':forms.TextInput(attrs={'class':'form-input'}),
            'middle_name':forms.TextInput(attrs={'class':'form-input'}),
            #'gruppa':forms.TextInput(attrs={'class':'form-input'}),
        }

    # def __init__(self, *args, **kwargs):
    #     # Вызываем родительский конструктор
    #     super().__init__(*args, **kwargs)
        
        # Проверяем, есть ли у формы данные (для валидации POST) или это новый объект.
        # self.instance.pk существует, если мы редактируем существующего пользователя.
        # if self.instance and self.instance.pk:
        #     # Проверяем статус пользователя
            # if self.instance.status == 'Студент':
            #     # Если студент - скрываем поле для преподавателей
            #     self.fields['groups_as_teacher'].widget = forms.HiddenInput()
            #     self.fields['groups_as_teacher'].required = False
                
            # elif self.instance.status == 'Преподаватель':
            #     # Если преподаватель - скрываем поле для студентов
            #     self.fields['group_as_student'].widget = forms.HiddenInput()
            #     self.fields['group_as_student'].required = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Проверяем, что форма привязана к существующему объекту в БД
        if self.instance and self.instance.pk:
            # Если пользователь - студент, удаляем поле для преподавателей
            if self.instance.status == 'Студент':
                if 'groups_as_teacher' in self.fields:
                    del self.fields['groups_as_teacher']
                if 'group_as_student' in self.fields:
                    del self.fields['group_as_student']
            
            # Если пользователь - преподаватель, удаляем поле для студентов
            elif self.instance.status == 'Преподаватель':
                if 'group_as_student' in self.fields:
                    del self.fields['group_as_student']
                



           