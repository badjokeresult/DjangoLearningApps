from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', showAllMovies),
    path('movie/<slug:slug_movie>', showMovie, name='movie-detail'),
    path('directors', showAllDirectors),
    path('directors/<int:id>', showDirector, name='director-detail'),
    path('actors', showAllActors),
    path('actors/<int:id>', showActor, name='actor-detail')
]
