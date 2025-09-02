from django.contrib import admin
from django.urls import path
from . import views
# from views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home)      
    #if we use (from views import home) then we can use home without using views.home
]
