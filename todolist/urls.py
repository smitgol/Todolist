"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from profiles_api import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_form
from usermanagement import views as user_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todolist', views.TodolistViewSet)
router.register('user', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo', include('profiles_api.urls'), name="todolist"),
    path('register/', user_views.register, name="register"),
    path('', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('api/', include(router.urls)),
    path('api/login/', views.UserLoginApiView.as_view(), name="loginapi"),

]
