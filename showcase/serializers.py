from .models import Film
from rest_framework import serializers

class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'imageUrl', 'trailerUrl', 'genre','released_date']