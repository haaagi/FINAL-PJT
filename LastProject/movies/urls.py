from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'movies'

urlpatterns = [
    path('movies/', views.movielist),
    path('movie_detail/<int:movie_id>', views.movie_detail),
    # path('recommend/<int:user_id>', views.recommend),
]