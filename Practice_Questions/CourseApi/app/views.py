from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def CourseView(request):
    if request.method =="GET":
     course = Course.objects.all()
     serializer = CourseSerializer(course,many=True)
     return Response(serializer.data)
    elif request.method =="POST":
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response(serializer.erros)


@api_view(['GET','DELETE','PUT'])
def CourseDetailView(request,pk):
    try:
        course2 = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method =="DELETE":
        course2.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)
    elif request.method =="GET":
        serializer = CourseSerializer(course2)
        return Response(serializer.data)
    elif request.method =="PUT":
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.erros)