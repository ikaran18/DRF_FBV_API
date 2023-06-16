from rest_framework import serializers
from .models import *

# Create Your Serializer Here

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
     
    def update(self, students , validated_data):
        newstudents = Student(**validated_data)
        newstudents.id = students.id
        newstudents.save()
        return newstudents
        