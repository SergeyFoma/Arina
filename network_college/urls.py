from django.urls import path
from . import views

app_name = "network_college"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('electronic_diary/', views.electronic_diary, name='electronic_diary'),
    # Адрес для API (откуда JS будет брать данные)
    path('api/diary/', views.diary_data_api, name='diary_data'),
]