from django.http import HttpResponse

def hello_page(request):
    return HttpResponse("<h1>Hello, World!</h1>")