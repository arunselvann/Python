from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('create/', views.posts_create, name='create'),
    path('<slug>/', views.posts_detail, name='detail'),
    path('delete/<slug>', views.posts_delete, name='delete'),
    path('edit/<slug>', views.posts_update, name='update'),
]

