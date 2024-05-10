from django.shortcuts import render
# import HttpResponse from django
from django.http import HttpResponse

# Create your views here.

def home(request):
    print("Hello World")
    return HttpResponse("Hello World")