from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Movie
from .serializers import MovieSerializer, ReviewSerializer, ReviewCreationSerializer, MovieReviewSerializer
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


# @api_view(['GET'])
# def movie_detail(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     serializer = MovieSerializer(instance=movie)
#     return Response(serializer.data)


# @api_view(['POST'])
# def recommend(request, user_id):
#     # 좋아요 나이 팔로우 
#     user = get_object_or_404(User, id=user_id)

@api_view(['GET'])
def movie_like(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    # if movie.like_users.filter(id=user.id).exists():
    #     movie.like_users.remove(user)
    # else:
    movie.like_users.add(user)
    return Response(status=200)


@api_view(['POST'])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = ReviewCreationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, movie=movie)
        review_list_serializer = MovieReviewSerializer(instance=movie)
        return Response(data=review_list_serializer.data, status=200)
    return Response(status=400)

@api_view(['GET'])
def review_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieReviewSerializer(instance=movie)
    return Response(data=serializer.data)





