from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('home', views.home, name='home'),
    path('info', views.info),
    path("showform", views.showform, name="showform"), 
    path("getform/", views.get_form_details, name= 'getformby' ),
]
