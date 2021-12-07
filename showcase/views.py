from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Film
from .serializers import FilmAllSerializer,FilmDetailSerializer
from rest_framework import filters,generics

# Create your views here.
class FilmList(APIView):

    
    def get(self,request):

            film = Film.objects.all()
            sort = request.GET.get("sort",None)
            print(sort)
            if sort == "year_ascending":
                film = Film.objects.all().order_by("released_year")
            elif sort == "year_descending":
                film = Film.objects.all().order_by("-released_year")
            
            serializers = FilmAllSerializer(film, many=True)
            return Response({"status" : 200,
                "message" : "Success",
                "data":serializers.data})
            
    def post(self,request):

        film = Film.objects.all()      
        serializers = FilmAllSerializer(film, many=True)
        film_exist = False
        for data in serializers.data:
            if request.data['title'] == data['title'] and request.data['released_year'] == data['released_year']:
                film_exist=True
                break
            else:
                film_exist=False
            
        if not film_exist:
            film = Film.objects.create(
                title = request.data['title'],
                imageUrl = request.data['imageUrl'],
                trailerUrl = request.data['trailerUrl'],
                genre = request.data['genre'],
                released_year = request.data['released_year'],
            )
            serializers = FilmDetailSerializer(film)
            return Response({"status" : 201,
        "message" : "Created",
        "data":serializers.data})

        else:
            return Response({
                "status" : 204,
        "message" : "Success no data, existed film"})
        

class FilmSearchFilter(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
        
class FilmLikeDislike(APIView):
    def put(self, request, id,action):
        try :
            film = Film.objects.get(id=id)
            if action == "like":
                film.like += 1
            elif action == "dislike":
                film.dislike += 1
            else:
                return Response({
                    "error": "hanya bisa like atau dislike"
                })
            film.save()
        except Film.DoesNotExist:
             return Response({
                "error" : "film tidak ditemukan"
            })

        serializers = FilmDetailSerializer(film)
        return Response({
            "status" : 201,
            "message" : "update successfull",
            "data" : serializers.data
        })
class FilmDetail(APIView):
    def get(self, request, id):
        #TODO Implement get by title
        try :
            film = Film.objects.get(id=id)
            serializers = FilmDetailSerializer(film)
        except Film.DoesNotExist :
            return Response({
                "error" : "film tidak ditemukan"
            })
        return Response({
            "status" : 200,
            "message" : "get film success",
            "data" : serializers.data
        })
    def delete(self, request, id) :
        try:
            
            film = Film.objects.get(id=id)
            film.delete()

            return Response({
                "status" : 201,
                "message" : "delete success",
            })
        except Film.DoesNotExist:
            return Response({
                "error" : "film tidak ditemukan"
            })
    
    