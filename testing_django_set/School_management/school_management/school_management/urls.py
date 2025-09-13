from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),



    path('', views.home),



    path('teacher/', include('teacher.urls')),

]
