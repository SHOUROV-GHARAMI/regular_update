from django.http import HttpResponse   # ✅ you must have this import

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")