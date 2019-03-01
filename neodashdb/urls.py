"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import ListCreateAssetsView, LoginView, ListCreateScansView, ListCreateVulnsView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('assets', ListCreateAssetsView.as_view(), name="assets-all"),
    path('scans', ListCreateScansView.as_view(), name="scans-all"),
    path('vulns', ListCreateVulnsView.as_view(), name="vulns-all"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
]
