from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

#from network_college.models import Status
class Group(models.Model):
    number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.number
    
# Предмет
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# График
class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='schedules')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.date} | {self.subject} | {self.group}"

# Назначение 
class Assignment(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='assignments')
    topic = models.CharField(max_length=200)

    def __str__(self):
        return self.topic
    


# CHOICES = [
#     ('student', 'Студент'),
#     ('teacher', 'Преподаватель'),
#     ('admin', 'Администратор'),
# ]
class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='avatar/%Y/%m/%d', 
                blank=True, null=True, verbose_name='Avatar')
    # status = models.CharField(max_length=150, choices = CHOICES, default = 'status', blank=True, null=True, 
    #             verbose_name='Статус')
    status = models.CharField(max_length=150, blank=True,null=True)
    middle_name = models.CharField(max_length=150, blank=True, null=True, 
                verbose_name='Отчество')
    # gruppa = models.CharField(max_length=150, blank=True, null=True, 
    #             verbose_name='Группа')
    number = models.IntegerField(verbose_name="Личный номер", blank=True, null=True,)
    #role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    group_as_student = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    # Если нужно хранить связь "преподаватель — группы"
    groups_as_teacher = models.ManyToManyField(Group, related_name='teachers', blank=True)
    #status_user = models.ForeignKey(Status, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователя"

    def __str__(self):
        return self.username
    

class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    value = models.IntegerField()  # например, 1-5

    def __str__(self):
        return f"{self.student} — {self.value}"


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='avatar/%Y/%m/%d', blank=True, null=True, verbose_name='Avatar')
#     status = models.CharField(max_length=150, blank=True, null=True, verbose_name='Статус')
#     middle_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Отчество')

#     def __str__(self):
#         return self.user.username
    

'''
    Логика связей:

Student → Group: Ученик состоит в одной группе.
Group → Schedule: У группы есть расписание занятий.
Schedule → Subject: Каждое занятие относится к предмету.
Schedule → Assignment: На занятии могут быть задания.
Assignment → Grade: За задание выставляются оценки.
Grade → Student: Оценка принадлежит конкретному студенту.
'''