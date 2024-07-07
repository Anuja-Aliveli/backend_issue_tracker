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

from authentication.forgot_password import forgot_login_password, reset_forgot_password
from authentication.login import user_login
from authentication.registration import user_registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_registration),
    path('login/', user_login),
    # Forgot Password APIS
    path('forgot_password_check_email/', forgot_login_password),
    path('reset_user_password/', reset_forgot_password)
]