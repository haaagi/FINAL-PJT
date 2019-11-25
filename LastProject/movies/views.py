from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
@api_view(['GET'])
def movielist(request):
    movie = get_object_or_404(Movie, id=1)
    serializer = MovieSerializer(instance=movie)
    return Response(serializer.data)
    
