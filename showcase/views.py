from django.shortcuts import render
from django.http import HttpResponse
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
        film = Film.objects.create(
            title = request.data['title'],
            imageUrl = request.data['imageUrl'],
            trailerUrl = request.data['trailerUrl'],
            like=0,
            genre = request.data['genre'],
            released_date = request.data['released_date'],
        )

        serializers = FilmAllSerializer(film) 
        return Response({"status" : 201,
            "message" : "Created",
            "data":serializers.data})

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

    def put(self, request, id):
        try :
            pass
            ## hanya contoh
            # TODO: Implement tambah like 
            # film = Film.objects.get(id=id)
            # film.name = request.data['name']
            # film.author = request.data['author']
            # film.volume = request.data['volume']
            # film.total_page = request.data['total_page']
            # film.publisher = request.data['publisher']
            # film.published_date = request.data['published_date']
            # film.save()
        except Film.DoesNotExist:
             return Response({
                "error" : "buku tidak ditemukan"
            })

        # serializers = FilmDetailSerializer(film)
        # return Response({
        #     "status" : 201,
        #     "message" : "update successfull",
        #     "data" : serializers.data
        # })


    def delete(self, request, id) :
        film = Film.objects.get(id=id)
        film.delete()

        return Response({
            "status" : 201,
            "message" : "delete success",
        })