from .models import Film
from rest_framework import serializers

class FilmAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'imageUrl', 'trailerUrl','like','dislike','genre','released_year']

class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'imageUrl', 'trailerUrl','like','dislike','genre','released_year']