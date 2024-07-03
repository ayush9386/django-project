from django.shortcuts import render
from .serializers import AuthorSerializer , BookSerializer
from rest_framework import generics
from .models import Author , Book
from rest_framework.pagination import  PageNumberPagination , LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class AuthorPagination(PageNumberPagination):
    page_size = 2
class BookPagination(LimitOffsetPagination):
    page_size = 3






class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['firstname']


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer   