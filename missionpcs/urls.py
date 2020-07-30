"""missionpcs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from userapp import views as user_view

urlpatterns = [
    path('delete/<int:pk>/',user_view.delete_timetable,name='delete'),
    path('edit/<int:pk>/',user_view.edit,name='edit'),
    path('',user_view.home,name = 'home'),
    path('add/',user_view.addtimetable,name='add'),
    path('register/',user_view.registration,name = 'registration'),
    path('register/login/', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userapp/logout.html'), name="logout"),
    path('register/login/timetable/', user_view.timetable, name='timetable'),
    path('admin/', admin.site.urls),

]
