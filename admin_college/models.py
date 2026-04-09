from django.db import models
import random

def veri():
    x=['A','a','B','b','C','c','D','d','E','e','W','w']
    for i in range(0,10):
        x.append(str(i))
    return ''.join(random.sample(x,10))


# def veri():
#     x=[]
#     for i in range(0,10):
#         x.append(str(i))
#     print("XXXXX: ", x)
#     a=''.join(x)
#     return a
    

class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество')
    first_name = models.CharField(max_length=100, verbose_name='Фамилия')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    verification_number = models.CharField(max_length=150, default=veri, verbose_name='Верификационный номер')

    def save(self,*args, **kwargs):
        if not self.verification_number:
            self.verification_number = veri() 
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def save(self, *args, **kwargs):
        if not self.verification_number:
            self.verification_number=veri()
        super().save(*args, **kwargs)
