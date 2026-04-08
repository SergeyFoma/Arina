from django.urls import path
from . import views

app_name='admin_college'

urlpatterns = [
    path('check/', views.check,name='check'),
]
