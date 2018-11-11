from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from posts.api import views

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='list'),
    path('create/', views.PostCreateAPIView.as_view(), name='create'),
    path('delete/<slug>/', views.PostDestroyAPIView.as_view(), name='delete'),
    path('edit/<slug>/', views.PostUpdateAPIView.as_view(), name='update'),
    path('<slug>/', views.PostDetailAPIView.as_view(), name='detail'),
]

