from django.urls import path
from .views import *
urlpatterns = [
    path('',CourseView),
    path('course/<int:pk>',CourseDetailView),
]
