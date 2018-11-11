from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('api/posts/', include(('posts.api.urls', 'posts'), namespace='posts-api')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)