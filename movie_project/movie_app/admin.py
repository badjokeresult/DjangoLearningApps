from django.contrib import admin
from .models import Movie, Director, Actor
from django.db.models import QuerySet
# Register your models here.

admin.site.register(Director)
admin.site.register(Actor)

class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('to-50', 'Низкий'),
            ('from-50-to-70', 'Средний'),
            ('from-70-to-90', 'Высокий'),
            ('from-90', 'Высочайший')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == 'to-50':
            return queryset.filter(rating__lte=50)
        if self.value() == 'from-50-to-70':
            return queryset.filter(rating__gt=50).filter(rating__lte=70)
        if self.value() == 'from-70-to-90':
            return queryset.filter(rating__gt=70).filter(rating__lte=90)
        if self.value() == 'from-90':
            return queryset.filter(rating__gt=90)
        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ['actors']
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'rating', 'year', 'budget', 'director', 'rating_status']
    list_editable = ['rating', 'year', 'director']
    ordering = ['-rating', 'name']
    list_per_page = 10
    actions = ['set_dollars', 'set_euros', 'set_rubles']
    search_fields = ['name']
    list_filter = [RatingFilter]

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Очень плохо'
        if mov.rating < 70:
            return 'Проходняк'
        if mov.rating <= 85:
            return 'Очень хорошо'
        return 'Потрясающе'

    @admin.action(description='Установить валюты в доллары')
    def set_dollars(self, request, qs: QuerySet):
        count = qs.update(currency=Movie.USD)
        self.message_user(request,
                          f'Было обновлено {count} записей.')

    @admin.action(description='Установить валюты в евро')
    def set_euros(self, request, qs: QuerySet):
        count = qs.update(currency=Movie.EUR)
        self.message_user(request,
                          f'Было обновлено {count} записей.')

    @admin.action(description='Установить валюты в рубли')
    def set_rubles(self, request, qs: QuerySet):
        count = qs.update(currency=Movie.RUB)
        self.message_user(request,
                          f'Было обновлено {count} записей.')