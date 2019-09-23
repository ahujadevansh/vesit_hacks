from django.urls import path
from . import views as task_views

urlpatterns = [
    path('task/', task_views.TaskView.as_view(), name='task_tasks'),
    path('incharge/',task_views.get_details,name='incharge'),
    path('incharge/<int:pk>/', task_views.SubordinateDetails.as_view(), name='task-subordinate_detail'),
    path('graph/',task_views.GraphViewUser.as_view(), name='tasks-graph_user'),
    path('graph/<int:pk>',task_views.GraphView.as_view(), name='tasks-graph')
    ]