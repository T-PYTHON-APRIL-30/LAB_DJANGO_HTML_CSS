from . import views
from django.urls import path

app_name="dream"

urlpatterns=[
    path("", views.home,name="home")
]