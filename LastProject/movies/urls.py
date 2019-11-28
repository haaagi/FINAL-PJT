from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'movies'

urlpatterns = [
    path('movies/', views.movielist),
    # path('movie_detail/', views.movie_detail),
    # path('recommend/<int:user_id>', views.recommend),
    path('movielike/<int:movie_id>/', views.movie_like),
    path('reviews/new/<int:movie_id>/', views.review_create),
    path('<int:movie_id>/reviews/', views.review_list),
]