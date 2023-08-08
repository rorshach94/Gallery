"""
URL configuration for bnw_captures project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home),
    path('explore/', views.explore),
    path('about/', views.about),
    path('contact/', views.contact),
    path('explore/bnw_captures/templates/story1.html', views.illusion),
    path('explore/bnw_captures/templates/story2.html', views.abstract),
    path('explore/bnw_captures/templates/story3.html', views.mandala),
    path('explore/bnw_captures/templates/story4.html', views.gothic),
    path('explore/bnw_captures/templates/story5.html', views.macabre),
    path('explore/bnw_captures/templates/story6.html', views.loop),
    path('explore/bnw_captures/templates/story7.html', views.manuscript),
    path('explore/bnw_captures/templates/story8.html', views.ghoul),
    path('explore/bnw_captures/templates/story9.html', views.darknet),
    path('explore/bnw_captures/templates/story10.html', views.ai),
]
