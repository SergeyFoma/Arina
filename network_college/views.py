from django.http import JsonResponse
from django.shortcuts import render

from users.models import Grade

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

from django.contrib.auth.decorators import login_required

# НОВАЯ ФУНКЦИЯ: Только для отрисовки HTML-страницы
@login_required
def electronic_diary(request):
    """Отображает страницу дневника"""
    # Просто рендерим шаблон. Данные загрузит JS.
    return render(request, 'network_college/electronic_diary.html')

# НОВАЯ ФУНКЦИЯ: Только для API-запросов (JSON)
@login_required
def diary_data_api(request):
    """API-эндпоинт для получения оценок студента в формате JSON"""
    student = request.user

    grades_qs = Grade.objects.filter(student=student).select_related(
        'assignment__schedule__subject'
    )
    
    data = []
    for grade in grades_qs:
        data.append({
            'date': grade.assignment.schedule.date.strftime('%d.%m.%Y'),
            'subject': grade.assignment.schedule.subject.name,
            'value': grade.value,
            'topic': grade.assignment.topic,
        })
    
    return JsonResponse({'grades': data})