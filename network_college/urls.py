from django.urls import path
from . import views

#app_name = "network_college"

urlpatterns = [
    path('', views.index, name='index'),
]