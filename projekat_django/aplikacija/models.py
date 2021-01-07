from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=70)
    year = models.PositiveSmallIntegerField(default=0)
    synopsis = models.TextField(default='')

    def __str__(self):
        return self.name + '(' + str(self.year) + ')'


class Comment(models.Model):
    content = models.TextField(default='')
    time = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return str(self.user) + ' - ' + str(self.movie)
