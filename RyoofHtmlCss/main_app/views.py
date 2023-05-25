from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
# Create your views here.


def home_page(request: HttpRequest):
    #to use template , we use render and pass in the path to the template
    return render(request, "main_app/home.html")