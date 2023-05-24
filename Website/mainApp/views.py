from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def homePage(request:HttpRequest):
    return render(request,'mainApp/index.html')
