from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

#admin.site.register(CustomUser, UserAdmin)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'image', 'first_name','last_name','middle_name', 'status', 'email']
