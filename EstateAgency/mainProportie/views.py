from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def homePage(request: HttpRequest):
    return render(request, "mainProportie/homePage.html")
