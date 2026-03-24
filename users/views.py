from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import RegisterForm, LoginForm, ProfileUserForm#, UserImageForm, UserProfileForm,
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from users.models import Profile
from users.models import CustomUser
from django.contrib.auth.models import User

# Импорты для смены пароля
from django.contrib.auth import update_session_auth_hash #предотвращает принудительный выход пользователя после смены пароля.
from django.contrib.auth.forms import PasswordChangeForm # встроенная форма в фреймворке Django, предназначенная для обработки запросов на изменение пароля.
from django.contrib.auth.mixins import LoginRequiredMixin #ограничивает доступ к смене пароля только авторизованными пользователями. Если представление использует этот миксин, все запросы от пользователей, не прошедших аутентификацию, будут перенаправляться на страницу входа или отображаться с ошибкой HTTP 403 Forbidden в зависимости от параметра raise_exception.
#from django.shortcuts import render, redirect
from django.views.generic import FormView #Представление, отображающее форму. В случае ошибки повторно отображает форму с ошибками проверки; в случае успешного выполнения перенаправляет на новый URL


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('REGISTER= ', request.user)
            # Profile.objects.create(user_id=request.user.id)
            return redirect(reverse("users:login_user"))
    else:
        form = RegisterForm()
        #print(form)

    context = {
        "form": form,
    }
    return render(request, "users/register_user.html", context)





def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request, username=username, password=password)            
            #Profile.objects.create(user_id=user.id)
            if user and user.is_active:
                login(request,user)
                return redirect(reverse("users:profile"))
    else:
        form = LoginForm() 
    context={
        'form':form,
    }

    return render(request, "users/login_user.html", context)



@login_required
def profile(request):
    user=request.user
    prof = CustomUser.objects.get(username=user.username)
    # Проверяем существование пользователя и создаём его, если нет
    # user_id, created = CustomUser.objects.get_or_create(
    #     user_id=user.id,
    # )
    # if created:
    # # Установим пароль новому пользователю
    #     # user.set_password('secure_password_123')
    #     # user.save()
    #     print("Пользователь создан!")
    # else:
    #     print("Пользователь уже существует!")
    # # if not prof:
    # #     Profile.objects.create(user_id=user.id)
    # prof = CustomUser.objects.get(username=user.username)
    
    if request.method == 'POST':
        form = ProfileUserForm(request.POST, request.FILES, instance=user)
        #form_image = UserImageForm(request.POST, request.FILES, instance=prof)
        if form.is_valid():# and form_image.is_valid():
            form.save()
            
            #form_image.save()
            #return HttpResponseRedirect("users:profile")
    else:
        form = ProfileUserForm(instance=user)
        #form_image = UserImageForm(instance=prof)
    return render(request, "users/profile.html",{'form':form, 'prof':prof,})# 'form_image':form_image})


def logout_user(request):
    logout(request)
    return redirect(reverse("network_college:index"))


class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/change_password.html'
    form_class = PasswordChangeForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Обновляем сессионную аутентификацию, чтобы предотвратить выход пользователя
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)

# def password_reset(request):
#     return render(request, "users/password_reset.html")