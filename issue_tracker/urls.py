"""
URL configuration for study_smart_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from authentication.forgot_password import check_email, reset_forgot_password
from authentication.login import user_login
from authentication.registration import user_registration
from project_manager.create_project import create_project, get_project_details, update_project_details
from project_manager.projects import get_project_cards_data, get_projects_table_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_registration),
    path('login/', user_login),
    # Forgot Password APIS
    path('check_email/', check_email),
    path('reset_user_password/', reset_forgot_password),
    # Project APIS 
    path('create_project/', create_project),
    path('get_project/', get_project_details),
    path('update_project', update_project_details),
    path('projects/', get_projects_table_data),
    path('projects_cards/', get_project_cards_data)
]