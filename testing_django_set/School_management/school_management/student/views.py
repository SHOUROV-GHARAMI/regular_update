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
    marks = [
        {"id": 1, "subject": "Math", "marks": 80},
        {"id": 2, "subject": "English", "marks": 65},
        {"id": 3, "subject": "Science", "marks": 85},
        {"id": 4, "subject": "History", "marks": 75},
        {"id": 5, "subject": "Bio", "marks": 85},
        {"id": 6, "subject": "Social_Science", "marks": 35},
        {"id": 7, "subject": "Math", "marks": 59},
    ]

    return render(
        request,
        "student/index.html",
        {
            "marks": marks,
            "age": 20,
            "Name": "Md Abdullah All Baki",
            "lst": ["apple", "orange", "banana"],
        },
    )


def home(request):
    return HttpResponse("I am in student home page")
