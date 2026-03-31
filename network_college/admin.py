from django.contrib import admin
from .models import *

'''
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display=['name', 'slug']
    prepopulated_fields={'slug':('name',)}
# Register your models here.
'''