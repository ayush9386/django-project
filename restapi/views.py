from django.shortcuts import render
from django.http import JsonResponse ,HttpResponse 
from restapi.models import employee ,student
from restapi.serializers import studentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status 
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

@api_view(['GET' , 'POST'])
def student_view(request):
    if request.method == 'GET':
        students = student.objects.all()
        serializer_used = studentSerializer(students , many = True)
        #print(serializer_used)
        return Response(serializer_used.data)
    
    if request.method == 'POST':
        serializer_used = studentSerializer(data = request.data)
        if serializer_used.is_valid():
            serializer_used.save()
            return Response(serializer_used.data , status=status.HTTP_201_CREATED)
        return Response(serializer_used.errors , status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET' , 'PUT' , 'DELETE'])
def student_detail(request , pk):
    try:
        student_obj = student.objects.get(pk = pk)
    except student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = studentSerializer(student_obj)
        return Response(serializer.data )
    
    elif request.method == 'PUT':
        serializer = studentSerializer(student_obj , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    elif  request.method =='DELETE':
        student_obj.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
