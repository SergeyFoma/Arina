from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['number',]

#admin.site.register(CustomUser, UserAdmin)
class CustomUserAdmin(UserAdmin):
    # Добавьте ваши новые поля в список отображаемых в общем списке
    list_display = UserAdmin.list_display + ('image','middle_name', 'status', 'number', 'group_as_student')#, 'status_user')

    # Добавьте ваши поля в формы создания и редактирования
    # fieldsets — для редактирования существующего пользователя
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': ('image','middle_name', 'status', 'number', 'group_as_student', 'groups_as_teacher')#, 'status_user'),
        }),
    )

    # add_fieldsets — для создания нового пользователя
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('image','middle_name', 'status', 'number', 'group_as_student', 'groups_as_teacher')#, 'status_user'), # Добавьте поля, которые нужны при создании
        }),
    )
    def display_groups(self, obj):
        # Возвращает список групп через запятую для конкретного пользователя (obj)
        return ", ".join([group.number for group in obj.groups_as_teacher.all()])
    
    display_groups.short_description = 'Группы'  # Название колонки в админке

admin.site.register(CustomUser, CustomUserAdmin)

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'image', 'first_name','last_name','middle_name', 'status', 'email']
