from django.contrib import admin
from django.urls import path,include
from practice import views

urlpatterns =[
    path('' , views.post_passenger_details , name = 'passenger' ),
    path('<str:firstname>' , views.passenger_detail , name = 'passenger_detail' ),
]