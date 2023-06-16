from django.urls import path
from .views import *
urlpatterns = [
    path('',CompanyListView),
    path('company/<int:pk>',CompanyDetailView)
]
