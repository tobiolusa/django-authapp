from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', views.index, name='index'),
    path('login/', views.loginpage, name='loginpage'),
    path('register/', views.register, name='register'),
    path('reset-password/', views.reset_password, name='reset-password'),
]