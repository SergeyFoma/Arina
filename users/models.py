from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='avatar/%Y/%m/%d', 
                blank=True, null=True, verbose_name='Avatar')
    status = models.CharField(max_length=150, blank=True, null=True, 
                verbose_name='Статус')
    middle_name = models.CharField(max_length=150, blank=True, null=True, 
                verbose_name='Отчество')
    gruppa = models.CharField(max_length=150, blank=True, null=True, 
                verbose_name='Группа')



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='avatar/%Y/%m/%d', blank=True, null=True, verbose_name='Avatar')
#     status = models.CharField(max_length=150, blank=True, null=True, verbose_name='Статус')
#     middle_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Отчество')

#     def __str__(self):
#         return self.user.username
    

