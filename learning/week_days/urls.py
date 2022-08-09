from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('hello/', greeting),
    path('<int:day>/', getToDoListByNumber),
    path('<str:day>/', getToDoList, name='todo_week_list'),
]