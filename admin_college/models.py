from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество')
    first_name = models.CharField(max_length=100, verbose_name='Фамилия')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    verification_number = models.CharField(max_length=150, verbose_name='Верификационный номер')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
