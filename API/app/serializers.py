from rest_framework import serializers
from .models import *

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=55)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=55)


class EmployeeSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=55)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=55)
    
    def create(self, validated_data):
        return EmployeeModel.objects.create(**validated_data)
    
    def update(self, employee, validated_data):
        newemployee = EmployeeModel(**validated_data)
        newemployee.id = employee.id
        newemployee.save()
        return newemployee
        