from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user/<id>', views.UserView.as_view(), name='user'),
]
