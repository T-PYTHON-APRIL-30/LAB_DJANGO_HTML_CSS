from django.urls import path
from. import views

urlpatterns= [
    path("" , views. home_welcome, name= "home_welcome"),
]