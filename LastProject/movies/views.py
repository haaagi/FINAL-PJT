from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Movie

# Create your views here.


@csrf_exempt
def movielist(request):
    if request.method == 'GET':
        movie = Movie.objects.get(id=1)
        return movie