from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users_logout'),
    path('profile/', users_views.ProfileView.as_view(), name='users_profile'),
    path('', users_views.home, name='home'),
    path('register/', users_views.RegisterView.as_view(),name='register'),
]