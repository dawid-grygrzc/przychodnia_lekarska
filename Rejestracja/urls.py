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
from rej.views import home_view, \
    weryfikacja_view, rejestracja_view, wizyta_view, pesel_view, register_view, profile_view
from django.contrib.auth import views as auth_views
from django.views.i18n import JavaScriptCatalog



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('weryfikacja/<int:id>/', weryfikacja_view, name='weryfikacja'),
    path('rejestracja/<int:id>/', rejestracja_view, name='rejestracja'),
    path('wizyta/<int:id>', wizyta_view, name='wizyta'),
    path('pesel/<int:id>', pesel_view, name='pesel'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog')
]
