from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.
class ListEmployeeAPIView(ListAPIView):
    """This endpoint list all of the available Employees from the database"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeAPIView(ListAPIView):
    """This endpoint single Employee from the database"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CreateEmployeeAPIView(CreateAPIView):
    """This endpoint allows for creation of a Employee"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UpdateEmployeeAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Employee by passing in the id of the Employee to update"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeleteEmployeeAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Employee from the database"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer