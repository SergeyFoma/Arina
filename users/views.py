from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("users:login_user"))
    else:
        form = RegisterForm()
        print(form)

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
    return render(request, "users/profile.html")


def logout(request):
    return render(request, "users/logout.html")
