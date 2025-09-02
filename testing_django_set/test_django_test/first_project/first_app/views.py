from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return render(request,'index.html')

def home(request):
    return render(request,'page1.html')

def about(requenst):
    return HttpResponse("about page")