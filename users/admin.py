from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

#admin.site.register(CustomUser, UserAdmin)
class CustomUserAdmin(UserAdmin):
    # Добавьте ваши новые поля в список отображаемых в общем списке
    list_display = UserAdmin.list_display + ('image','middle_name', 'status', 'gruppa', 'number')#, 'status_user')

    # Добавьте ваши поля в формы создания и редактирования
    # fieldsets — для редактирования существующего пользователя
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': ('image','middle_name', 'status', 'gruppa', 'number')#, 'status_user'),
        }),
    )

    # add_fieldsets — для создания нового пользователя
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('image','middle_name', 'status', 'gruppa', 'number')#, 'status_user'), # Добавьте поля, которые нужны при создании
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'image', 'first_name','last_name','middle_name', 'status', 'email']
