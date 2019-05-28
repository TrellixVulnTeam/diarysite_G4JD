"""foodproject URL Configuration

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
import diaryapp.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', diaryapp.views.lists, name='lists'),
    path('new/',diaryapp.views.new, name = 'new'),
    path('create',diaryapp.views.create, name = 'create'),
    path('<int:blog_id>', diaryapp.views.detail, name = "detail"),
    path('blog/edit/<int:blog_id>', diaryapp.views.edit, name = 'edit'),
    path('blog/delete/<int:blog_id>', diaryapp.views.delete, name = 'delete'),
    path('signup/', diaryapp.views.signup, name = "signup"),
    path('login/', diaryapp.views.login, name = "login"),
    path('logout/', diaryapp.views.logout, name = "logout"),
    path('accounts/',include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)