from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request: HttpResponse):
    return render (request, 'app_general/index.html')



def about(request: HttpResponse):
    return render (request, 'app_general/about.html')



def contact(request: HttpResponse):
    return render(request, 'app_general/contact.html')