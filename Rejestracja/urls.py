"""Rejestracja URL Configuration

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
from django.contrib.auth import views as auth_views
from django.views.i18n import JavaScriptCatalog
from rej.views import register_view, home_view, visit_view, profile_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', home_view, name='home'),
    path('visit/<int:id>', visit_view, name='visit'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('profile/', profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
