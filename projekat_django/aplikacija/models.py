from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=70)
    year = models.PositiveSmallIntegerField
    synopsis = models.TextField


class Comment(models.Model):
    username = models.CharField
    content = models.TextField
    time = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
