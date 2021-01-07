from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Movie
# Create your views here.


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Movie reviews'})
    else:
        return redirect('aplikacija:movies')


def movies(req):
    tmp = Movie.objects.all()
    return render(req, 'movies.html', {'movies': tmp})


def movie(req, id):
    tmp = get_object_or_404(Movie, id=id)
    return render(req, 'movie.html', {'movie': tmp, 'page_title': tmp.name})