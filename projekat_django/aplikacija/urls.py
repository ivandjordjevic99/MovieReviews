from django.urls import path
from . import views

app_name = 'aplikacija'
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movie/<int:id>/', views.movie, name='movie'),
    path('movie/<int:id>/comments', views.comments, name='comments')
]