from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def movielist(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(instance=movie)
    return Response(serializer.data)
