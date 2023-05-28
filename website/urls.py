from. import views
from django.urls import path

app_name='website'

urlpatterns=[
    path('today/',views.today ,name='today'),
]
urlpatterns=[
    path('home/',views.home ,name='home'),
]