from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Student Learning Management App</h1>")
