"""blogs_news URL Configuration

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
from django.urls import path
from . import views
from .views import register


urlpatterns = [
    path('news_list', views.news_list, name='news_list'),
    path('', register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('news/<int:article_id>/', views.news_detail, name='news_detail'),
    path('bloglist/', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('blog/<int:blog_id>/delete/', views.blog_delete, name='blog_delete'),
]

