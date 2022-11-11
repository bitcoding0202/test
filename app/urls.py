from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.RegisterPage,name='register-form'),
    path('',views.home,name="home"),
]

