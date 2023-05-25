from django.urls import path
from . import views

name = "realestate_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),

]