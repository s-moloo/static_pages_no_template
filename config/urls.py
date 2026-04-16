from django.contrib import admin
from django.urls import path
from static_pages_1 import views

urlpatterns = [
    path('', views.home, name='home'),   
    path('about/', views.About, name="about"),
    path('contact/', views.Contact, name="contact"),
    path('programs/', views.Programs, name="programs"),
]
