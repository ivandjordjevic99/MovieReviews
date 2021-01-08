from django.urls import path
from . import views

app_name = 'aplikacija'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.user_register, name='user_register'),
    path('new_movie/', views.new_movie, name='new_movie'),
    path('movies/', views.movies, name='movies'),
    path('movie/<int:id>/', views.movie, name='movie'),
    path('movie/delete/<int:id>/', views.delete_movie, name='delete_movie'),
    path('movie/edit/<int:id>/', views.edit_movie, name='edit_movie'),
    path('movie/<int:id>/comments', views.comments, name='comments'),
    path('movie/<int:id>/new_comment', views.new_comment, name='new_comment')
]