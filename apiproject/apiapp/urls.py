
from django.urls import path
from . import views

urlpatterns = [

    path('sendData/',views.sendData)
   
]