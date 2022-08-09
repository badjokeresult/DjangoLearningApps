from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
# Create your views here.


def showAllMovies(request):
    movies = Movie.objects.all()
    for movie in movies:
        movie.save()
    return render(request, 'movie_app/all_movies.html', context={
        'movies': movies
    })


def showMovie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie,
    })

def showAllDirectors(request):
    dirs = Director.objects.all()
    for dir in dirs:
        dir.save()
    return render(request, 'movie_app/all_directors.html', context={
        'dirs': dirs
    })


def showDirector(request, id):
    dir = Director.objects.all()[id-1]
    return render(request, 'movie_app/one_director.html', context={
        'dir': dir
    })

def showAllActors(request):
    acts = Actor.objects.all()
    for act in acts:
        act.save()
    return render(request, 'movie_app/all_actors.html', context={
        'acts': acts
    })

def showActor(request, id:int):
    act = Actor.objects.all()[id-1]
    return render(request, 'movie_app/one_actor.html', context={
        'act': act
    })
