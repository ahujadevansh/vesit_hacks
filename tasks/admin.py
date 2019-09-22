from django.contrib import admin
from .models import Task, WeeklyReport
# Register your models here.
admin.site.register(Task)
admin.site.register(WeeklyReport)