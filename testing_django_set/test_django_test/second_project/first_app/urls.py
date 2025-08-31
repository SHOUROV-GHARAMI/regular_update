from django.contrib import admin
from django.urls import path, include

from.import views 

urlpatterns = [
    path('', views.first_app, name=''),
    path('home/', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('detail/', include('detail.urls'))
]