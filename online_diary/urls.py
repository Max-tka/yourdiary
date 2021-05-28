"""online_diary URL Configuration

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
from django.urls import path
from yourdiary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('profile/', views.profile_page, name='profile'),
    path('agreement/', views.agreement_page, name='agreement'),
    path('logout/', views.logout_page, name='logout'),
    path('createtask/', views.task_create_page, name='createtask'),
    path('settings/', views.settings_page, name='settings'),
    path('change_password/', views.change_password, name='change_password'),
    path('change_email/', views.change_email, name='change_email'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
