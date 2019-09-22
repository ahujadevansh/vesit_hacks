from django.urls import path
from . import views as task_views

urlpatterns = [
    path('task/', task_views.TaskView.as_view(), name='task_tasks'),
]