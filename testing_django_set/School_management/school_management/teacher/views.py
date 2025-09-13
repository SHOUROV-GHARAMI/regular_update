from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return HttpResponse("I am in teacher profile")

def home(request):
    return HttpResponse("I am in teacher home page")

def profile(request):
    return render(request, 'teacher/index.html')

