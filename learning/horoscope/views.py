from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

zodiac = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'
}


types = {
    'fire': ('aries', 'leo', 'sagittarius'),
    'earth': ('taurus', 'virgo', 'capricorn'),
    'air': ('gemini', 'libra', 'aquarius'),
    'water': ('cancer', 'scorpio', 'pisces')
}


def index(request):
    data = {
        'zodiac': list(zodiac)
    }
    return render(request, 'horoscope/index.html', context=data)


def getSignByDate(request, month:int, day:int):
    sign = ''
    if month == 1:
        if day in range(1, 22):
            sign = 'capricorn'
        elif day in range(21, 32):
            sign = 'aquarius'
    elif month == 2:
        if day in range(1, 19):
            sign = 'aquarius'
        elif day in range(20, 30):
            sign = 'pisces'
    elif month == 3:
        if day in range(1, 20):
            sign = 'pisces'
        elif day in range(21, 32):
            sign = 'aries'
    elif month == 4:
        if day in range(1, 21):
            sign = 'aries'
        elif day in range(21, 31):
            sign = 'taurus'
    elif month == 5:
        if day in range(1, 22):
            sign = 'taurus'
        elif day in range(22, 32):
            sign = 'gemini'
    elif month == 6:
        if day in range(1, 22):
            sign = 'gemini'
        elif day in range(22, 31):
            sign = 'cancer'
    elif month == 7:
        if day in range(1, 23):
            sign = 'cancer'
        elif day in range(23, 32):
            sign = 'leo'
    elif month == 8:
        if day in range(1, 22):
            sign = 'leo'
        elif day in range(22, 32):
            sign = 'virgo'
    elif month == 9:
        if day in range(1, 24):
            sign = 'virgo'
        elif day in range(24, 31):
            sign = 'libra'
    elif month == 10:
        if day in range(1, 24):
            sign = 'libra'
        elif day in range(24, 32):
            sign = 'scorpio'
    elif month == 11:
        if day in range(1, 23):
            sign = 'scorpio'
        elif day in range(23, 31):
            sign = 'sagittarius'
    elif month == 12:
        if day in range(1, 23):
            sign = 'sagittarius'
        elif day in range(23, 32):
            sign = 'capricorn'
    else:
        return HttpResponseNotFound(f'Введена некорректная дата - месяц: {month}, день: {day}')

    if not sign:
        return HttpResponseNotFound(f'Введена некорректная дата - месяц: {month}, день: {day}')
    else:
        url = reverse('horoscope-name', args=(sign, ))
        return HttpResponseRedirect(url)


def getTypes(request):
    response = '<ul>'
    for type in types:
        response += f"<li><a href='{type}'>{type.capitalize()}</a></li>"
    return HttpResponse(response + '</ul>')


def getType(request, element:str):
    response = ''
    for sign in types[element]:
        url = reverse('horoscope-name', args=(sign, ))
        response += f"<li><a href='{url}'>{sign.capitalize()}</a></li>"
    return HttpResponse('<ul>' + response + '</ul>')


def getInfo(request, sign:str):
    try:
        description = zodiac[sign]
    except KeyError:
        description = None

    data = {
        'zodiac': zodiac,
        'description': description,
        'sign': sign
    }
    return render(request, 'horoscope/info_zodiac.html', data)


def getInfoByNumber(request, sign:int):
    try:
        url = reverse('horoscope-name', args=(list(zodiac)[sign-1], ))
        return HttpResponseRedirect(url)
    except IndexError:
        return HttpResponseNotFound(f'Неизвестный порядковый номер - {sign}')