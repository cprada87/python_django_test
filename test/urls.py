"""test URL Configuration

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

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls), # Admin site
    path(r'api/', include('api.urls')), # Api Root

    path(r'api-token-auth/', obtain_jwt_token), # Obtain Json Web Token
    path(r'api-token-refresh/', refresh_jwt_token), # Refresh Json Web Token
    path(r'api-token-verify/', verify_jwt_token), # Verify Json Web Token

    path(r'', include('django.contrib.auth.urls')),

]
