from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('games.urls')),
    path('publishers/', include('publishers.urls')),
    path('categories/', include('categories.urls')),
]
