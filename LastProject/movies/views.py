from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

from django.contrib.auth import get_user_model 

User = get_user_model()

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


# @api_view(['POST'])
# def recommend(request, user_id):
#     # 좋아요 나이 팔로우 
#     user = get_object_or_404(User, id=user_id)








