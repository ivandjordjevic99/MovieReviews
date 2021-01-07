from django.forms import ModelForm
from .models import Movie, Comment


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'year', 'synopsis']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
