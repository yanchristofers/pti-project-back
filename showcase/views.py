from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Film
from .serializers import FilmDetailSerializer
# Create your views here.

class FilmList(APIView):
    def get(self,request):
        film = Film.objects.all()
        serializers = FilmDetailSerializer(film, many=True)
        return Response({"status" : 200,
            "message" : "Success",
            "data":serializers.data})

    def post(self,request):
        film = Film.objects.create(
            title = request.data['title'],
            imageUrl = request.data['imageUrl'],
            trailerUrl = request.data['trailerUrl'],
            genre = request.data['genre'],
            released_date = request.data['released_date'],
        )

        serializers = FilmDetailSerializer(film) 
        return Response({"status" : 201,
            "message" : "Created",
            "data":serializers.data})

    def delete(self, request, id) :
        film = Film.objects.get(id=id)
        film.delete()

        return Response({
            "status" : 200,
            "message" : "delete success",
        })
