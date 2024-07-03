from django.urls import path , include
from django.contrib import  admin
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students' , views.StudentViewSet)


urlpatterns = [
    #path('students/' , views.StudentList.as_view()),
    #path('students/<int:pk>' , views.StudentDetail.as_view()),
    path('' , include(router.urls))
]


