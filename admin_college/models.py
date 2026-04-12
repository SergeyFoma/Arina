from django.db import models
#import random
from django.utils import timezone
import secrets

# def veri():
#     x=['A','a','B','b','C','c','D','d','E','e','W','w']
#     for i in range(0,10):
#         x.append(str(i))
#     return ''.join(random.sample(x,10))
    

# class Teacher(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Имя')
#     middle_name = models.CharField(max_length=100, verbose_name='Отчество')
#     first_name = models.CharField(max_length=100, verbose_name='Фамилия')
#     date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
#     verification_number = models.CharField(max_length=150, default=veri, verbose_name='Верификационный номер')

#     class Meta:
#         verbose_name = 'Преподаватель'
#         verbose_name_plural = 'Преподаватели'

#     def save(self, *args, **kwargs):
#         if not self.verification_number:
#             self.verification_number=veri()
#         super().save(*args, **kwargs)

# def generate_code(self):
#         """Генерирует уникальный код."""
#         self.invite_code = secrets.token_urlsafe(16) # Генерирует безопасную строку
#         print('Code: ',self.invite_code)
class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя',blank=True, null=True)
    middle_name = models.CharField(max_length=100, verbose_name='Отчество',blank=True, null=True)
    first_name = models.CharField(max_length=100, verbose_name='Фамилия',blank=True, null=True)
    #date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    invite_code = models.CharField(
        max_length=32,
        unique=True,
        help_text="Уникальный код для регистрации",
        blank=True, 
        null=True,
        #default=generate_code
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Код активен и может быть использован",
        blank=True, 
        null=True
    )
    used_at = models.DateTimeField(
        null=True, 
        blank=True,
        help_text="Время, когда код был использован",
    )

    # def generate_code(self):
    #     # Генерируем URL-безопасный токен (32 байта -> 43 символа в base64url)
    #     self.token = secrets.token_urlsafe(32)
    #     self.save()

    def save(self, *args, **kwargs):
        # Генерируем токен только если он ещё не задан (например, при создании)
        if not self.invite_code:
            self.invite_code = secrets.token_urlsafe(8)
            # В редких случаях коллизии можно добавить цикл, но для 32 байт это почти невозможно
        super().save(*args, **kwargs)

    # def generate_code(self):
    #     """Генерирует уникальный код."""
    #     self.invite_code = secrets.token_urlsafe(16) # Генерирует безопасную строку
    #     print('Code: ',self.invite_code)

    # def save(self, *args, **kwargs):
    #     if not self.invite_code:
    #         self.invite_code=generate_code()
    #     super().save(*args, **kwargs)
    
    def use_code(self):
        """
        Маркирует код как использованный.
        Устанавливает флаг is_active в False и записывает время использования.
        """
        if self.is_active:
            self.is_active = False
            self.used_at = timezone.now()
            self.save()