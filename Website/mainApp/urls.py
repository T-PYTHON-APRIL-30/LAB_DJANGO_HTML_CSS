from . import views
from django.urls import path

appName = 'mainApp'

urlpatterns = [
    path('',views.homePage, name='homePage')
]
