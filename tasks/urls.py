from django.urls import path
from . import views as task_views

urlpatterns = [
    path('task/', task_views.TaskListView.as_view(), name='task_tasks_list'),
    path('task/<int:pk>/', task_views.TaskView.as_view(), name='task_task_detail'),
    path('incharge/',task_views.InchargeView.as_view(),name='incharge'),
    path('incharge/<int:pk>/', task_views.SubordinateDetails.as_view(), name='task-subordinate_detail'),
    path('graph/',task_views.GraphViewUser.as_view(), name='tasks-graph_user'),
    path('graph/<int:pk>',task_views.GraphView.as_view(), name='tasks-graph')
    ]