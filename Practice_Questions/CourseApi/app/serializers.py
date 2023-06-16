from rest_framework import serializers
from .models import Course

# Create your serializer here.

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
    
    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    
    def update(self,course2,validated_data):
        newcourse = Course(**validated_data)
        newcourse.id = course2.id
        newcourse.save()
        return newcourse
