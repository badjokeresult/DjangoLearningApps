from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from math import pi
from django.urls import reverse
# Create your views here.

def redirectRectangle(request, width:int, height:int):
    url = reverse('calculate_geometry_function', args=(width, height))
    return HttpResponseRedirect(url)


def redirectSquare(request, width:int):
    url = reverse('calculate_geometry_function', args=(width, ))
    return HttpResponseRedirect(url)


def redirectCircle(request, radius):
    #url = reverse('calculate_geometry_function', args=(radius, ))
    #return HttpResponseRedirect(url)
    return render(request, 'geometry/circle.html')


def getRectangleArea(request, width:int, height:int):
    #if width < 0 or height < 0:
    #    return HttpResponseBadRequest('<h1>Значения длины и ширины не могут быть отрицательными числами</h1>')
    #return HttpResponse(f'<h1>Площадь прямоугольника размером {width}*{height} = {width * height}</h1>')
    return render(request, 'geometry/rectangle.html')


def getSquareArea(request, width):
    #if width < 0:
    #    return HttpResponseBadRequest('<h1>Длина стороны квадрата не может быть отрицательной</h1>')
    #return HttpResponse(f'<h1>Площадь квадрата размером {width}*{width} = {width * width}</h1>')
    return render(request, 'geometry/square.html')


def getCircleArea(request, radius):
    #if radius < 0:
    #    return HttpResponseBadRequest('<h1>Радиус круга не может быть отрицательной</h1>')
    #return HttpResponse(f'<h1>Площадь круга радиусом {radius} = {round(pi * radius * radius, 3)}</h1>')
    return render(request, 'geometry/circle.html')