from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()

    context = {
        "form": form,
    }
    return render(request, "users/register.html", context)


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user and user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = LoginForm() 

    return render(request, "users/login.html")


def profile(request):
    return render(request, "users/profile.html")


def logout(request):
    return render(request, "users/logout.html")
