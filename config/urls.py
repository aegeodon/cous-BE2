"""
URL configuration for config project.

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

from coususers.views import kakao_login, user_my_detail, user_patch
from courses.views import course_access_one, course_access
from scraps.views import scrap_access, scrap_access_one

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('auth/kakao/login', kakao_login),
    path('users', user_patch),
    path('users/me', user_my_detail),
    
    path('courses', course_access),
    path('courses/<int:pk>', course_access_one),
    
    
    path('scraps', scrap_access),
    path('scraps/<int:pk>', scrap_access_one)
]
