from django.shortcuts import render
from django.http import HttpResponse



def profile(request):
    return HttpResponse("I am in student profile")

def home(request):
    return HttpResponse("I am in student home page")