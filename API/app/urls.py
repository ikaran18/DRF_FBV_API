from django.urls import path
from .views import *
urlpatterns = [
    path('api/employee/',employeeListView,name='home'),
    path('api/employee/<int:pk>',employeeDetailView,name='employeedetail'),
    path('api/users/',UserViewList,name='employeelist'),
]
