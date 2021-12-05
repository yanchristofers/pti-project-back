from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=1000)
    trailerUrl = models.CharField(max_length=1000)
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    genre = models.CharField(max_length=200)
    released_year = models.IntegerField()
