from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

from .forms import CommentForm, MovieForm
from .models import Movie
from .models import Comment
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


def comments(req, id):
    tmp = Comment.objects.filter(movie=id)
    return render(req, 'comments.html', {'comments': tmp})


def new_comment(req, id):
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            m = Movie.objects.get(id=id)
            c = Comment(content=form.cleaned_data['content'], user=req.user, movie=m)
            c.save()
            return redirect('aplikacija:comments', id)
        else:
            return render(req, 'newComments.html', {'form': form, 'id': id})
    else:
        form = CommentForm()
        return render(req, 'newComment.html', {'form': form, 'id': id})


def new_movie(req):
    if req.method == 'POST':
        form = MovieForm(req.POST)

        if form.is_valid():
            m = Movie(name=form.cleaned_data['name'], year=form.cleaned_data['year'], synopsis=form.cleaned_data['synopsis'])
            m.save()
            return redirect('aplikacija:movies')
        else:
            return render(req, 'newMovie.html', {'form': form})
    else:
        form = MovieForm()
        return render(req, 'newMovie.html', {'form': form})
