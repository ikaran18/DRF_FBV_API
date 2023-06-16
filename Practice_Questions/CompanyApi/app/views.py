from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .models import Company
from .serializers import CompanySerializer

# Create your views here.

# ---------------------------Non-Primary Key Based ----------------------------------

@api_view(['GET','POST'])
def CompanyListView(request):
    if request.method =="GET":
        company = Company.objects.all()
        serializer = CompanySerializer(company,many = True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# --------------------------Primary Key Based ---------------------------------------

@api_view(['GET','DELETE','PUT'])
def CompanyDetailView(request,pk):
    try :
        company_detail = Company.objects.get(pk=pk)
    except Company.DoesNotExist :
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =="GET":
        serializer = CompanySerializer(company_detail)
        return Response(serializer.data)
    
    elif request.method =="DELETE":
        company_detail.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    
    elif request.method =="PUT":
        serializer = CompanySerializer(company_detail,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)