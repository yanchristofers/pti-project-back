from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=1000)
    trailerUrl = models.CharField(max_length=1000)
    genre = models.CharField(max_length=200)
    released_date = models.CharField(max_length=2000)
