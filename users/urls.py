from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('sigup/', views.signup, name='signup'),
    path('', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
