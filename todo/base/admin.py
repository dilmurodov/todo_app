from django.contrib import admin
from . models import *
# Register your models here.


class TasksAdmin(admin.ModelAdmin):
    list_display= ('title', 'user', 'create', 'complete')
admin.site.register(Tasks, TasksAdmin)