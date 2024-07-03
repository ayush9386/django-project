from django.shortcuts import render
from restapi.models import student
from restapi.serializers import studentSerializer
from restapi.models import student
from rest_framework.response import Response
from rest_framework import status , generics, mixins , viewsets
from rest_framework.views import APIView
from django.http import Http404


# "HERE WE ARE PERFORMING VIEWSETS"
class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer

# class StudentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = student.objects.all()
#     serializer_class = studentSerializer



## "HERE WE ARE PERFORMING CLASS BASED VIEW USING DIFFERENT GENERICS METHOD "
# class StudentList(generics.ListCreateAPIView):
#     queryset = student.objects.all()
#     serializer_class = studentSerializer

# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = student.objects.all()
#     serializer_class = studentSerializer

## "HERE WE ARE PERFORMING CLASS BASED VIEW WITH MIXINS"
# class StudentList(mixins.ListModelMixin , mixins.CreateModelMixin  , generics.GenericAPIView):
#     queryset = student.objects.all()
#     serializer_class = studentSerializer

#     def get(self , request):
#         return self.list(request)
    
#     def post(self , request):
#         return self.create(request)
    
# class StudentDetail(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView):
#     queryset = student.objects.all()
#     serializer_class = studentSerializer
    
#     def get(self , request , pk):
#         return self.retrieve(request , pk)
    
#     def put(self, request , pk):
#         return self.update(request, pk)
    
#     def delete(self , request , pk):
#         return self.destroy(request, pk) 





## "HERE WE ARE PERFORMING CLASS BASED VIEWS"
# class StudentList(APIView):
#     def get(self , request):
#         students = student.objects.all()
#         serializer = studentSerializer(students,  many = True)
#         return Response(serializer.data)
    
#     def post(self , request):
#         serializer = studentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'message' : ' the data  is saved',
#                 'response' : serializer.data
#             }
#             return Response(data , status = status.HTTP_201_CREATED)
        

# class StudentDetail(APIView):
#     def get_object(self , pk):
#         try: 
#             return student.objects.get(pk = pk)
#         except student.DoesNotExist:
#             raise Http404
        
#     def get(self , request , pk):
#         studentt =  self.get_object(pk)
#         serializer = studentSerializer(studentt)
#         return Response(serializer.data)
    
#     def put(self , request , pk):
#         studentt = self.get_object(pk)
#         serializer = studentSerializer( studentt, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data  )
#         return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
#     def delete(self , request, pk):
#         studentt = self.get_object(pk)
#         studentt.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
    
