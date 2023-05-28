from django.urls import path
from . import views

app_name = "mainProportie"

urlpatterns = [
path("", views.homePage, name="homePage")
]