from django.contrib import admin
from .models import Task


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'created_at', 'updated_at')

admin.site.register(Task, TaskModelAdmin)
