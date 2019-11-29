from django.contrib import admin
from django.urls import path
from Mao import views

urlpatterns = [
    path('1/', views.index),
]