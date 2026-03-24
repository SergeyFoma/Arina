from django.db import models
#from users.models import CustomUser

# Статус, Предметы, Группы, Расписание, Домашние задания, Оценки

class Status(models.Model):
    name = models.CharField(max_length=150, verbose_name="Статус")
    slug = models.SlugField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name
