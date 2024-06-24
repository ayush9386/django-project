from django.shortcuts import render
from django.http import JsonResponse ,HttpResponse , response
from restapi.models import employee ,student
from restapi.serializers import studentSerializer
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    return HttpResponse('here we will get familier with rest api')


# def employee(request):
def employee_detail(request):
    data = employee.objects.all()
    #print(data)
    response = {'employees' : list(data.values('name' , 'age', 'salary'))     
             }
    return JsonResponse(response)

#@api_view(['GET' , 'POST'])
def student_view(request):
    students = student.objects.all()
    #print(students)
    serializer_used = studentSerializer(students , many = True)
    print(serializer_used)
    #return response(serializer_used.data)
    return HttpResponse(serializer_used.data)