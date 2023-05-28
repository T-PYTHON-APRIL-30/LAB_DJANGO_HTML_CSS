from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
from datetime import datetime


# Create your views here.

def today(request:HttpResponse):
    today=datetime.today()
    #context={"today":today}
    return render(request,'website/today.html',{"today":today})
def home(request:HttpResponse):
    home=datetime.home()
    #context={"home":home}
    return render(request,'website/home.html',{"home":home})