from django.urls import path,include
from . import views as task_views

urlpatterns = [
    path('incharge/',task_views.get_details,name='incharge'),
]