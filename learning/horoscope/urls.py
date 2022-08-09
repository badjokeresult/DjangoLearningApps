from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='horoscope-index'),
    path('<int:month>/<int:day>/', getSignByDate),
    path('type/', getTypes),
    path('type/<str:element>/', getType),
    path('<int:sign>/', getInfoByNumber),
    path('<str:sign>/', getInfo, name='horoscope-name')
]