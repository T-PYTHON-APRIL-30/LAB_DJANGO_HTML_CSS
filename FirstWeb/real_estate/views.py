from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def realEstate(request:HttpRequest):
    return render(request,"real_estate/home.html")