from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
# Create your views here.

# ---------------------- Non-Primary Key Based Operations ----------------------------

@api_view(['GET','POST'])
def BookListView(request):
    if request.method == "GET":
     books = Book.objects.all()
     serializer = BookSerializer(books,many = True)
     return Response(serializer.data)
    elif request.method == "POST":
        serializer = BookSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)
    
# ---------------------- Primary Key Based Operations ----------------------------

@api_view(['GET','PUT','DELETE'])
def BookDetailView(request,pk):
    try:
        books = Book.objects.get(pk=pk)
    except Book.DoesNotExist :
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    if request.method =="GET":
        serializer = BookSerializer(books)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
         books.delete()
         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
         
     
    elif request.method =="PUT":
        serializer = BookSerializer( books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)