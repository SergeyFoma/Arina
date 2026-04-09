from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'middle_name', 'first_name', 'date', 'verification_number']
    readonly_fields = ('verification_number',)

# Register your models here.
