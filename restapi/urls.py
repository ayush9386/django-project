from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index , name  = 'index'),
    path('emp/' , views.employee_detail , name  = 'emp'),
    path('student/' , views.student_view , name  = 'student'),
    path('student/<int:firstname>' , views.student_detail , name  = 'student_detail'),
]