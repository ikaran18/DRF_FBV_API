from django.urls import path
from .views import *
# create your urls 

urlpatterns = [
    path('',StudentView),
    path('student/',StudentDetailView),
    path('student/<int:pk>',StudentDetailView),
]
