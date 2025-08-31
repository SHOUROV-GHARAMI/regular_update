from django.contrib import admin
from django.urls import path, include

from.import views 

urlpatterns = [
    path('', views.detail, name=''),
    path('showrov/', views.showrov, name='showrov'),
    path('imran/', views.imran, name="imran"),
]