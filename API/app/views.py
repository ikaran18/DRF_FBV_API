from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt 
from  rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.


def UserViewList(request):
        if request.method =="GET":
          users = User.objects.all()
          serializer = UserSerializer(users,many=True)
          return JsonResponse(serializer.data,safe=False)
  
  
#--------------------------Non-Primary Key Based Operation-------------------------
@csrf_exempt
def employeeListView(request):
        if request.method =="GET":
                employees = EmployeeModel.objects.all()
                serializer = EmployeeSerializer(employees,many=True)
                return JsonResponse(serializer.data,safe=False)
        elif request.method =="POST":
                jsonData= JSONParser().parse(request)
                serializer = EmployeeSerializer(data = jsonData)
                if serializer.is_valid():
                        serializer.save()
                        return JsonResponse(serializer.data,safe=False)
                else:
                     return JsonResponse(serializer.errors,safe = False)

#--------------------------Primary Key Based Operation-------------------------
@csrf_exempt
def employeeDetailView(request,pk):
        try:
                employee = EmployeeModel.objects.get(pk=pk)
                
        except EmployeeModel.DoesNotExist:
                return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        
        if request.method == "DELETE":
                 employee.delete()
                 return HttpResponse()
         
        elif request.method == "GET":
                serializer = EmployeeSerializer(employee)
                return JsonResponse(serializer.data,safe=False)
        
        elif request.method == "PUT":
                jsonData= JSONParser().parse(request)
                serializer = EmployeeSerializer(employee, data = jsonData)
                if serializer.is_valid():
                        serializer.save()
                        return JsonResponse(serializer.data,safe=False)
                else:
                     return JsonResponse(serializer.errors,safe = False)