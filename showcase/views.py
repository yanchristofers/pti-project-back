from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Film
from .serializers import FilmAllSerializer,FilmDetailSerializer
# Create your views here.

class FilmList(APIView):
    def get(self,request):
        #TODO Implement sort by like, implement sort descending and ascending released year
        film = Film.objects.all()
       
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


        

class FilmDetail(APIView):
    def get(self, request, id):
        #TODO Implement get by title
        try :
            film = Film.objects.get(id=id)
            serializers = FilmDetailSerializer(film)
        except Film.DoesNotExist :
            return Response({
                "error" : "buku tidak ditemukan"
            })
        return Response({
            "status" : 200,
            "message" : "get book success",
            "data" : serializers.data
        })

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


    def delete(self, request, id,action) :
        try:
            if action == "delete":
                film = Film.objects.get(id=id)
                film.delete()

                return Response({
                    "status" : 201,
                    "message" : "delete success",
                })
            else:
                return Response({
                    "status" : 204,
                    "message" : "/delete is required",
                })
        except Film.DoesNotExist:
            return Response({
                "error" : "film tidak ditemukan"
            })