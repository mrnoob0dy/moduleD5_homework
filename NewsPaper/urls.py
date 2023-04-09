"""NewsPaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from newapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('protect.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('newapp.urls')),
    path('accounts/', include('allauth.urls')),
    path('news/search/', Search.as_view(), name='search'),
    path('news/add/', PostsCreateView.as_view(), name='posts_create'),
    path('news/<int:pk>/edit/', PostsUpdateView.as_view(), name='posts_update'),
    path('news/<int:pk>/delete/', PostsDeleteView.as_view(), name='posts_delete'),
]
