from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

week = {
    'monday': '1. Сходить за продуктами 2. Почитать 3. Погулять 4. Подготовить дз в универ на вторник ',
    'tuesday': '1. Сходить на учёбу 2. Погулять 3. Учить Django ',
    'wednesday': 'Нет дел на среду ',
    'thursday': 'Нет дел на четверг ',
    'friday': 'Нет дел на пятницу ',
    'saturday': 'Нет дел на субботу ',
    'sunday': 'Нет дел на воскресенье '
}


def index(request):
    res = '<ul>'
    for day in week:
        url = reverse('todo_week_list', args=(day,))
        res += f"<li><a href='{url}'>{day.capitalize()}</a></li>"
    res += '</ul>'
    return HttpResponse(res)


def greeting(request):
    return render(request, 'week_days/greeting.html')


def getToDoList(request, day:str):
    try:
        return HttpResponse(week[day])
    except KeyError:
        return HttpResponseNotFound(f'Несуществующий день недели - {day.capitalize()}')


def getToDoListByNumber(request, day:int):
    try:
        url = reverse('todo_week_list', args=(list(week)[day-1], ))
        return HttpResponseRedirect(url)
    except IndexError:
        return HttpResponseNotFound(f'Несуществующий номер дня недели - {day}')

