"""Kullanıcılar için URL örüntülerini tanımlar."""
from django.urls import path,include
from . import views

app_name = 'users'

urlpatterns = [
    #Varsayılan auth urls'i dahil et.
    path('',include('django.contrib.auth.urls')),
    #Kayıt Sayfası
    path('register/', views.register,name = 'register'),
]
