from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Hello world!!!! </h1>")
def about(requst):
    return HttpResponse("<h2> About this page!! </h2>")