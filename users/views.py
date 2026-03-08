from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import UserProfileForm, RegisterForm, LoginForm, UserImageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # print('REGISTER= ', request.user.id)
            # Profile.objects.create(user_id=request.user.id)
            return redirect(reverse("users:login_user"))
    else:
        form = RegisterForm()
        #print(form)

    context = {
        "form": form,
    }
    return render(request, "users/register.html", context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request, username=username, password=password)
            print('Authenticated= ', user, user.id)
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
    print(type(request.user.id))
    prof = Profile.objects.get(user=user)
    print(type(prof.user_id))
    print(prof)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        form_image = UserImageForm(request.POST, request.FILES, instance=prof)
        if form.is_valid() and form_image.is_valid():
            form.save()
            
            form_image.save()
            #return HttpResponseRedirect("users:profile")
    else:
        form = UserProfileForm(instance=user)
        form_image = UserImageForm(instance=prof)
    return render(request, "users/profile.html",{'form':form, 'prof':prof, 'form_image':form_image})


def logout_user(request):
    logout(request)
    return redirect(reverse("network_college:index"))
