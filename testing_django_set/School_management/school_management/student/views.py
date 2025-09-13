from django.shortcuts import render
from django.http import HttpResponse


# def profile(request):
#     return HttpResponse("I am in student profile")


def profile(request):
    user_data = {
        "name": "Rahim",
        # "age" : 20
        "age": 30,
    }
    marks = {
        {"id": 1, "subject": "Math", "marks": 80},
        {"id": 2, "subject": "English", "marks": 90},
        {"id": 3, "subject": "Science", "marks": 85},
        {"id": 3, "subject": "History", "marks": 75},
        {"id": 4, "subject": "Bio", "marks": 65},
    }
    # return render(request, 'student/index.html', user_data, {"marks" : marks})
    return render(request, "student/index.html", {"marks": marks})


def home(request):
    return HttpResponse("I am in student home page")
