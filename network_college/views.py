from django.shortcuts import render

menu = ['Главная','О нас','Контакты','Вход', 'Регистрация', 'Выход', 'Преподаватели', 'Студенты']

def index(request):
    context = {
        'menu':menu,
    }
    return render(request,"network_college/index.html", context)

def about(request):
    context = {
        'menu':menu,
    }
    return render(request, 'network_college/about.html', context)