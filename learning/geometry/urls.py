from django.urls import path
from .views import *

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', getRectangleArea, name='calculate_geometry_function'),
    path('square/<int:width>/', getSquareArea, name='calculate_geometry_function'),
    path('circle/<int:radius>/', getCircleArea, name='calculate_geometry_function'),

    path('get_rectangle_area/<int:width>/<int:height>/', redirectRectangle),
    path('get_square_area/<int:width>/', redirectSquare),
    path('get_circle_area/<int:radius>/', redirectCircle)
]