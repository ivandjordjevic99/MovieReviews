from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

from .forms import CommentForm, MovieForm, RegisterForm
from .models import Movie
from .models import Comment
from django.contrib.auth.models import User
# Create your views here.


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Movie reviews'})
    else:
        return redirect('aplikacija:movies')


@login_required
def movies(req):
    tmp = Movie.objects.all()
    return render(req, 'movies.html', {'movies': tmp})


@login_required
def movie(req, id):
    tmp = get_object_or_404(Movie, id=id)
    return render(req, 'movie.html', {'movie': tmp, 'page_title': tmp.name})


@login_required
def comments(req, id):
    tmp = Comment.objects.filter(movie=id)
    m = Movie.objects.get(id=id)
    return render(req, 'comments.html', {'comments': tmp, 'movie': m})


@login_required
def new_comment(req, id):
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            m = Movie.objects.get(id=id)
            c = Comment(content=form.cleaned_data['content'], user=req.user, movie=m)
            c.save()
            return redirect('aplikacija:comments', id)
        else:
            return render(req, 'newComment.html', {'form': form, 'id': id})
    else:
        form = CommentForm()
        return render(req, 'newComment.html', {'form': form, 'id': id})


@permission_required('aplikacija.add_movie')
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


@permission_required('aplikacija.change_movie')
def edit_movie(req, id):
    if req.method == 'POST':
        form = MovieForm(req.POST)

        if form.is_valid():
            m = Movie.objects.get(id=id)
            m.name = form.cleaned_data['name']
            m.year = form.cleaned_data['year']
            m.synopsis = form.cleaned_data['synopsis']
            m.save()
            return redirect('aplikacija:movies')
        else:
            return render(req, 'editMovie.html', {'form': form, 'id': id})
    else:
        m = Movie.objects.get(id=id)
        form = MovieForm(instance=m)
        return render(req, 'editMovie.html', {'form': form, 'id': id})


@permission_required('aplikacija.delete_movie')
def delete_movie(req, id):
    to_delete = get_object_or_404(Movie, id=id)
    to_delete.delete()
    return redirect('aplikacija:movies')


def user_register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)


        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(req, 'register.html', {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(req, 'register.html', {
                    'form': form,
                    'error_message': 'Email already exists.'
                })

            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
            )

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']

            user.save()
            login(req, user)

            return redirect('aplikacija:movies')
        else:
            return render(req, 'register.html', {
                'form': form,
                'error_message': 'Error'
            })
    else:
        form = RegisterForm()
        return render(req, 'register.html', {'form': form})
