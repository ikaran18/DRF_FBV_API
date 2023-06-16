from django.urls import path
from .views import *


urlpatterns = [
    path('',BookListView,name='booklistview'),
    path('book/<int:pk>',BookDetailView,name='booklistview'),
]
