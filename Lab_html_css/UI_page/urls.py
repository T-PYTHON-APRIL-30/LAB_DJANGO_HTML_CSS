from django.urls import path
from . import views

nam_app = "UI_page"

urlpatterns = [
    path("home/", views.home_page, name= "home_page")
]