from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog', include('blog.urls')),
    path('about', include('about.urls')),
    path('contact', include('contact.urls')),
    path('photo', include('photo.urls')),
]
