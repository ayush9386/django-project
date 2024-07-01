from django.shortcuts import render
from django.http import request 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PassengerSerializer
from .models import  Passenger
# Create your views here.
@api_view([ 'GET', 'POST'])
def post_passenger_details(request):
    if request.method == 'POST':
        serializer = PassengerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status  = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        passenger = Passenger.objects.all()
        serializer = PassengerSerializer(passenger , many = True)
        return Response(serializer.data)
    


@api_view(['GET' , 'PUT' , 'DELETE'])
def passenger_detail(request , firstname):
    try:
        passenger = Passenger.objects.get(firstName = firstname)
    except Passenger.DoesNotExist:

        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        passenger.delete()
        data = {"message": "This is a custom response"}
        return Response(data , status = status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer =  PassengerSerializer(passenger)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = PassengerSerializer(passenger , data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"message": "data has been updated",
                    "passenger": serializer.data}
            return Response(data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)