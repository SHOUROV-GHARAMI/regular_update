from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def detail(request):
    return HttpResponse("Detail App")

def showrov(request):
    return HttpResponse("showrov page")

def imran(request):
    return HttpResponse("imran page")

