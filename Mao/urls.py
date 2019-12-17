from django.contrib import admin
from django.urls import path
from Mao import views

urlpatterns = [
    path('1/', views.index),
    path('2/', views.showdevice),
    path('3/', views.add_device),
    path('4/', views.show_type),
]
