from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer

# Create your views here.

# --------------------------Non-Primary Key Based View--------------------

@api_view(['GET','POST'])
def StudentView(request):
    if request.method =="GET":
       student = Student.objects.all()
       serializer = StudentSerializer(student,many=True)
       return Response(serializer.data)
    elif request.method =="POST":
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
            else:
                return Response(serializer.errors)

#-------------------Primary Key Based ------------------------------


@api_view(['GET','DELETE','PUT'])
def StudentDetailView(request,pk):
    try:
         students = Student.objects.get(pk=pk)
    except Student.DoesNotExist :
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    
    if request.method =="GET":
        serializer = StudentSerializer(students)
        return Response(serializer.data)
    
    if request.method =="DELETE":
        students.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)
    
    elif request.method =="PUT":
          serializer = StudentSerializer(students , data=request.data)
          if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
          else:
             return Response(serializer.errors)