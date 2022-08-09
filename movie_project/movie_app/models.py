from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.name} {self.surname}'
        return f'Актриса {self.name} {self.surname}'

    def getUrl(self):
        return reverse('actor-detail', args=(self.id, ))

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    slug = models.SlugField(default='', null=False)

    def getUrl(self):
        return reverse('director-detail', args=(self.id,))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euros'),
        (USD, 'Dollars'),
        (RUB, 'Rubles')
    ]


    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)
    slug = models.SlugField(default='', null=False)
    director = models.ForeignKey(Director, null=True, on_delete=models.CASCADE, blank=True)
    actors = models.ManyToManyField(Actor)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def getUrl(self):
        return reverse('movie-detail', args=(self.slug,))

    def __str__(self):
        return f'{self.name} {self.rating}%'
