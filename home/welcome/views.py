from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def welcome(request:HttpRequest):
    return render(request, "page/welcome.html")







