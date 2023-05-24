from django.urls import path
from . import views

app_name = "real_estate"

urlpatterns = [
    path("",views.realEstate,name="real_estate")
]