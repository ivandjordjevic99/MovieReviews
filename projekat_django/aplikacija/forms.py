from django.forms import ModelForm
from .models import Movie, Comment
from django import forms

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'year', 'synopsis']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))