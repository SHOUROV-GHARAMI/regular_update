from django.shortcuts import render
from django.http import HttpResponse  
#for importing HttpResponse from django

# Create your views here.
def first_app(request):
    return HttpResponse("First App")

def home(request):
    return HttpResponse("Home page")

def about(request):
    return HttpResponse("About page")

